"""
database.py

PostgreSQL database connection manager using psycopg2.

This module is responsible for establishing, maintaining, and
gracefully closing a single PostgreSQL database connection for
the application lifecycle.
"""

import psycopg2
from psycopg2.extensions import connection

from app.core.config import settings
from app.core.logger import get_logger


logger = get_logger(__name__)


class Database:
    """
    Database connection manager.

    Implements a simple singleton-like pattern to manage a single
    PostgreSQL database connection using psycopg2.
    """

    _connection: connection | None = None

    @classmethod
    def connect(cls) -> None:
        """
        Establish a PostgreSQL database connection.

        If a connection already exists, this method returns immediately.
        Otherwise, it initializes a new connection and validates it
        by executing a simple test query.

        Raises:
            psycopg2.OperationalError: If connection fails.
        """
        if cls._connection:
            logger.debug("PostgreSQL connection already initialized")
            return

        logger.info("Connecting to PostgreSQL")

        cls._connection = psycopg2.connect(
            settings.db_connection_str,
            connect_timeout=5,
        )
        cls._connection.autocommit = True

        # Verify connection
        with cls._connection.cursor() as cursor:
            cursor.execute("SELECT 1")

        logger.info("PostgreSQL connection successful")

    @classmethod
    def get_connection(cls) -> connection:
        """
        Retrieve the active PostgreSQL database connection.

        Returns:
            connection: Active psycopg2 connection.

        Raises:
            RuntimeError: If the database connection has not been initialized.
        """
        if not cls._connection:
            raise RuntimeError("Database connection not initialized")
        return cls._connection

    @classmethod
    def close(cls) -> None:
        """
        Close the active PostgreSQL database connection.

        Safely closes the connection if it exists and resets the
        internal reference.
        """
        if cls._connection:
            logger.info("Closing PostgreSQL connection")
            cls._connection.close()
            cls._connection = None
            logger.info("PostgreSQL connection closed")
