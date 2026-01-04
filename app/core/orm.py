"""
orm.py

SQLAlchemy ORM setup for FeedOrchestrator.

This module defines the SQLAlchemy engine, session factory,
and declarative base used across the application.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from app.core.config import settings
from app.core.logger import get_logger


logger = get_logger(__name__)

# SQLAlchemy engine (sync)
engine = create_engine(
    f"postgresql+psycopg2://"
    f"{settings.DB_USER}:{settings.DB_PASSWORD}"
    f"@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}",
    pool_pre_ping=True,
)

# Session factory
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)

# Declarative base
Base = declarative_base()
