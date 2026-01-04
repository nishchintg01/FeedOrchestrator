"""
logger.py

Provides centralized logging initialization and logger retrieval.

This module loads logging configuration from an external YAML file
and exposes helper functions to initialize logging and retrieve
module-specific loggers.
"""

import logging
import logging.config
from pathlib import Path

import yaml


# Path to logger configuration file (outside app directory)
LOG_CONFIG_PATH = Path(__file__).resolve().parents[2] / "logger_config.yaml"


def setup_logging() -> None:
    """
    Initialize application-wide logging configuration.

    Loads logging settings from an external YAML configuration file.
    This function should be called once during application startup.
    """
    if not LOG_CONFIG_PATH.exists():
        raise FileNotFoundError(
            f"Logging configuration file not found: {LOG_CONFIG_PATH}"
        )

    with open(LOG_CONFIG_PATH, "r", encoding="utf-8") as file:
        config = yaml.safe_load(file)

    logging.config.dictConfig(config)


def get_logger(name: str) -> logging.Logger:
    """
    Retrieve a configured logger instance.

    Args:
        name (str): Logger name, typically __name__.

    Returns:
        logging.Logger: Configured logger instance.
    """
    return logging.getLogger(name)
