"""
main.py

FastAPI application entry point for FeedOrchestrator.

This module initializes application-wide logging, manages the
application lifecycle, and ensures that critical dependencies
such as the PostgreSQL database connection are properly initialized
and shut down.
"""

from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.core.database import Database
from app.core.logger import setup_logging, get_logger
from app.api.health import router as health_router
from app.core.schema import create_schema

# Initialize logging configuration (YAML-based)
setup_logging()
logger = get_logger(__name__)


@asynccontextmanager
async def lifespan_event(app: FastAPI):
    """
    FastAPI lifespan context manager.

    Establishes the PostgreSQL database connection during application
    startup and ensures it is gracefully closed during shutdown.

    Raises:
        RuntimeError: If database initialization fails.
    """
    try:
        logger.info("Starting FeedOrchestrator application")
        Database.connect()
        create_schema()
        yield
    except Exception as exc:
        logger.exception("Application startup failed")
        raise RuntimeError("Application startup aborted") from exc
    finally:
        Database.close()
        logger.info("Application shutdown complete")


# -------------------------------------------------------------------
# FastAPI App Instance
# -------------------------------------------------------------------
app = FastAPI(
    title="FeedOrchestrator",
    lifespan=lifespan_event,
)

# Include API Endpoints from API Folder
app.include_router(health_router)

@app.get("/", tags=["health"])
async def home():
    """
    Health check endpoint.

    Returns:
        dict: Basic application status response.
    """
    return {
        "service": "FeedOrchestrator",
        "status": "running",
    }
