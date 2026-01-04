"""
ingestion_run.py

ORM model definition for ingestion job tracking.

This module defines the IngestionRun entity, which represents a single
execution of the scheduled ingestion process. It acts as the parent
record for source-level ingestion outcomes.
"""

from sqlalchemy import Column, Integer, Text, TIMESTAMP, Index
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.core.orm import Base


class IngestionRun(Base):
    """
    Ingestion run model.

    Represents a single scheduled ingestion execution. Aggregates
    source-level ingestion results for observability and debugging.
    """

    __tablename__ = "ingestion_runs"

    id = Column(Integer, primary_key=True)

    started_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    completed_at = Column(TIMESTAMP)

    status = Column(Text, nullable=False)  # success | partial | failed

    error_message = Column(Text)

    # -----------------------------
    # Relationships
    # -----------------------------
    source_runs = relationship(
        "IngestionSourceRun",
        back_populates="ingestion_run",
        cascade="all, delete-orphan",
    )

    __table_args__ = (
        Index("ix_ingestion_runs_started_at", "started_at"),
        Index("ix_ingestion_runs_status", "status"),
    )