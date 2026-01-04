"""
models package

Import all ORM models so that SQLAlchemy can register them
with the declarative Base metadata.
"""

from app.models.source import Source
from app.models.article import Article
from app.models.ingestion_run import IngestionRun
from app.models.ingestion_source_run import IngestionSourceRun

__all__ = [
    "Source",
    "Article",
    "IngestionRun",
    "IngestionSourceRun",
]
