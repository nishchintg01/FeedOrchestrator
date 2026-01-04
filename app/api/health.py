"""
health.py

Health check endpoints for the FeedOrchestrator service.

This module provides endpoints to verify application and
database readiness. These endpoints are intended for use
by load balancers, container orchestrators, and monitoring
systems.
"""

from fastapi import APIRouter, status

from app.core.database import Database
from app.core.logger import get_logger


router = APIRouter(tags=["health"])
logger = get_logger(__name__)


@router.get(
    "/health",
    status_code=status.HTTP_200_OK,
)
def health_check():
    """
    Application health check endpoint.

    Performs a lightweight database query to verify that the
    PostgreSQL connection is active and responsive.

    Returns:
        dict: Health status of the application.

    Raises:
        HTTPException: If the database is unreachable.
    """
    try:
        conn = Database.get_connection()
        with conn.cursor() as cursor:
            cursor.execute("SELECT 1")
        return {
            "status": "healthy",
            "database": "reachable",
        }
    except Exception:
        logger.exception("Health check failed")
    return {
        "status": "unhealthy",
        "database": "unreachable",
    }
