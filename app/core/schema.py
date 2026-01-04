"""
schema.py

ORM-based database schema bootstrap.
"""

# 👇 THIS IMPORT IS CRITICAL
import app.models  # noqa: F401

from app.core.orm import Base, engine
from app.core.logger import get_logger

logger = get_logger(__name__)


def create_schema() -> None:
    """
    Create database tables using SQLAlchemy ORM metadata.
    """
    logger.info("Creating database schema (ORM)")
    Base.metadata.create_all(bind=engine)
    logger.info("Database schema ready")
