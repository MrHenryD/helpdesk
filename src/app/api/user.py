import uuid

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy import select
from sqlalchemy.orm import Session

import models
import schemas
from core.database import get_db

router = APIRouter()


def _query_users(
    db: Session, user_id: uuid.UUID | None = None, name: str | None = None
):
    q = select(models.User)
    if user_id:
        q = q.where(models.User.id == user_id)
    if name:
        q = q.where(models.User.name == name)
    return q


@router.post("/")
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    q = _query_users(db, name=user.name)
    row = (await db.execute(q)).one_or_none()
    if row:
        raise HTTPException(status_code=400, detail="User exists")
    new_user = models.User(name=user.name)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return schemas.UserRead.model_validate(new_user)


@router.delete("/{user_id}")
async def delete_user(user_id: uuid.UUID, db: Session = Depends(get_db)):
    q = _query_users(db, user_id=user_id)
    row = (await db.execute(q)).scalar_one_or_none()
    if not row:
        raise HTTPException(status_code=404, detail="User not found")
    await db.delete(row)
    await db.commit()
    return JSONResponse(status_code=202, content={"message": "User deleted"})


@router.get("/{user_id}", response_model=schemas.UserRead)
async def read_user(user_id: uuid.UUID, db: Session = Depends(get_db)):
    q = _query_users(db, user_id=user_id)
    row = (await db.execute(q)).scalar_one_or_none()
    if not row:
        raise HTTPException(status_code=404, detail="User not found")
    return schemas.UserRead.model_validate(row)


@router.get("/", response_model=list[schemas.UserRead])
async def read_users(db: Session = Depends(get_db)):
    q = _query_users(db)
    rows = (await db.execute(q)).scalars().all()
    return [schemas.UserRead.model_validate(row) for row in rows]
