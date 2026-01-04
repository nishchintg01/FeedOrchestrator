"""
source.py

ORM model definition for feed sources.
"""

from sqlalchemy import (
    Boolean,
    Column,
    Float,
    Integer,
    Text,
    TIMESTAMP,
    Index
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.core.orm import Base


class Source(Base):
    """
    Feed source model.

    Represents a single content source (e.g., an RSS feed) that the
    system ingests articles from.
    """

    __tablename__ = "sources"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(Text, nullable=False)
    feed_url = Column(Text, nullable=False, unique=True)
    site_url = Column(Text)

    source_type = Column(Text, default="rss", nullable=False)
    source_weight = Column(Float, default=1.0)

    is_active = Column(Boolean, default=True, nullable=False)

    last_fetched_at = Column(TIMESTAMP)

    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    updated_at = Column(
        TIMESTAMP,
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    # -----------------------------
    # Relationships
    # -----------------------------
    articles = relationship(
        "Article",
        back_populates="source",
        passive_deletes=True,
    )

    __table_args__ = (
        Index("ix_sources_feed_url", "feed_url"),
        Index("ix_sources_is_active", "is_active"),
    )
