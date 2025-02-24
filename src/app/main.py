import logging

from fastapi import FastAPI, HTTPException
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider

from api import user
from core import metrics
from core.logger import setup_logger

# Setup Logging
logger = setup_logger(__name__)

# Create a Tracer
provider = TracerProvider()
trace.set_tracer_provider(provider)
tracer = trace.get_tracer(__name__)

# Initialize App
app = FastAPI()
app.include_router(user.router, prefix="/user")


@app.get("/health")
def healthcheck():
    logging.info("This is good, status remains healthy")
    return {"status": "healthy"}


@app.get("/400")
def generate_400_error():
    logging.error("This is bad, a 400 Error!")
    raise HTTPException(
        status_code=400,
        detail="400 Error",
    )


_ = metrics.get_instrumentator(app)
