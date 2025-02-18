from fastapi import FastAPI

from api import user

app = FastAPI()

app.include_router(user.router, prefix="/user")


@app.get("/health")
def healthcheck():
    return {"status": "healthy"}
