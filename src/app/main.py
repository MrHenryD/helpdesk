import logging

from fastapi import FastAPI, HTTPException
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider

from api import user
from core import metrics

# Create a Logger
logger = logging.getLogger(__name__)

# Create a Tracer
provider = TracerProvider()
trace.set_tracer_provider(provider)
tracer = trace.get_tracer(__name__)

# Initialize App
app = FastAPI()
app.include_router(user.router, prefix="/user")


@app.get("/health")
def healthcheck():
    logger.info("This is good, status remains healthy")
    return {"status": "healthy"}


@app.get("/400")
def generate_400_error():
    logger.error("This is bad, a 400 Error!")
    raise HTTPException(
        status_code=400,
        detail="400 Error",
    )


_ = metrics.get_instrumentator(app)
