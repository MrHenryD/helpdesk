import uuid

from pydantic import BaseModel, ConfigDict


class UserCreate(BaseModel):
    name: str


class UserRead(BaseModel):
    # required for converting from SQLAlchemy model
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    name: str | None = None
