"""
article.py

ORM model definition for ingested articles.
"""

from sqlalchemy import (
    Column,
    Float,
    ForeignKey,
    Integer,
    Text,
    TIMESTAMP,
    ARRAY,
    Index
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.core.orm import Base


class Article(Base):
    """
    Article model.

    Represents a single ingested article, including its full content,
    metadata, and ranking-related attributes.
    """

    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)

    source_id = Column(
        Integer,
        ForeignKey("sources.id", ondelete="CASCADE"),
        nullable=False,
    )

    url = Column(Text, nullable=False, unique=True)
    canonical_url = Column(Text)

    title = Column(Text, nullable=False)
    summary = Column(Text)
    content = Column(Text)

    author = Column(Text)
    language = Column(Text)

    tags = Column(ARRAY(Text))
    categories = Column(ARRAY(Text))

    content_length = Column(Integer)
    reading_time_minutes = Column(Integer)

    published_at = Column(TIMESTAMP)
    ingested_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    updated_at = Column(
        TIMESTAMP,
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    rating = Column(Float)
    source_weight = Column(Float)
    freshness_score = Column(Float)
    quality_score = Column(Float)
    final_score = Column(Float)

    # -----------------------------
    # Relationships
    # -----------------------------
    source = relationship(
        "Source",
        back_populates="articles",
    )

    __table_args__ = (
        Index("ix_articles_url", "url"),
        Index("ix_articles_source_id", "source_id"),
        Index("ix_articles_published_at", "published_at"),
        Index("ix_articles_final_score", "final_score"),
    )
