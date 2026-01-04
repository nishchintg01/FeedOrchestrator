"""
ingestion_source_run.py

ORM model definition for source-level ingestion tracking.

This module defines the IngestionSourceRun entity, which captures
the outcome of ingesting a single source as part of an ingestion run.
"""

from sqlalchemy import (
    Column,
    Integer,
    Text,
    TIMESTAMP,
    ForeignKey,
    Index
)
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.core.orm import Base


class IngestionSourceRun(Base):
    """
    Source-level ingestion run model.

    Represents the ingestion outcome for a single source during
    a specific ingestion run.
    """

    __tablename__ = "ingestion_source_runs"

    id = Column(Integer, primary_key=True)

    ingestion_run_id = Column(
        Integer,
        ForeignKey("ingestion_runs.id", ondelete="CASCADE"),
        nullable=False,
    )

    source_id = Column(
        Integer,
        ForeignKey("sources.id", ondelete="CASCADE"),
        nullable=False,
    )

    started_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    completed_at = Column(TIMESTAMP)

    status = Column(Text, nullable=False)  # success | failed

    articles_fetched = Column(Integer, default=0)
    articles_inserted = Column(Integer, default=0)
    articles_updated = Column(Integer, default=0)

    error_message = Column(Text)

    # -----------------------------
    # Relationships
    # -----------------------------
    ingestion_run = relationship(
        "IngestionRun",
        back_populates="source_runs",
    )

    source = relationship(
        "Source",
        passive_deletes=True,
    )
    
    __table_args__ = (
        Index("ix_isr_ingestion_run_id", "ingestion_run_id"),
        Index("ix_isr_source_id", "source_id"),
        Index("ix_isr_status", "status"),
    )
