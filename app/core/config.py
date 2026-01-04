"""
config.py

This module handles application configuration management.

It loads environment variables from a `.env` file and exposes a centralized
`Settings` class that provides database configuration values required by
the application. This ensures configuration is environment-agnostic and
keeps sensitive information out of the codebase.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file at application startup
load_dotenv()


class Settings:
    """
    Application configuration settings.

    This class loads database-related configuration values from environment
    variables (optionally sourced from a .env file). It centralizes all
    configuration required for connecting to the PostgreSQL database.

    Attributes:
        DB_HOST (str): Database host name or IP address.
        DB_PORT (str): Database port number.
        DB_NAME (str): Name of the PostgreSQL database.
        DB_USER (str): Database user name.
        DB_PASSWORD (str): Database user password.
    """

    DB_HOST: str = os.getenv("POSTGRES_HOST", "localhost")
    DB_PORT: str = os.getenv("POSTGRES_PORT", "5432")
    DB_NAME: str = os.getenv("POSTGRES_DB", "database")
    DB_USER: str = os.getenv("POSTGRES_USER", "postgres")
    DB_PASSWORD: str = os.getenv("POSTGRES_PASSWORD", "postgres")

    @property
    def db_connection_str(self) -> str:
        """
        Construct a PostgreSQL connection string.

        Returns:
            str: A psycopg2-compatible PostgreSQL connection string
                 containing host, port, database name, user, and password.
        """
        return (
            f"host={self.DB_HOST} "
            f"port={self.DB_PORT} "
            f"dbname={self.DB_NAME} "
            f"user={self.DB_USER} "
            f"password={self.DB_PASSWORD}"
        )


# Singleton-like settings object used across the application
settings = Settings()
