from enum import Enum
from functools import lru_cache
from typing import Any

import yaml
from pydantic import BaseSettings, Field, PostgresDsn


class LogLevels(str, Enum):
    """Enum of permitted log levels."""

    debug = "debug"
    info = "info"
    warning = "warning"
    error = "error"
    critical = "critical"


class UvicornSettings(BaseSettings):
    """Settings for uvicorn server"""

    host: str
    port: int
    log_level: LogLevels
    reload: bool


class ApiConfigSettings(BaseSettings):
    """Settings for FastAPI Server"""

    title: str = ""
    description: str = ""
    version: str
    docs_url: str
    debug: bool


class LoggingConfigSettings(BaseSettings):
    """Settings for loguru"""

    custom_log_level: bool
    log_level: str = ""
    file_path: str = ""


class DatabaseConnectionSettings(BaseSettings):
    """Settings for database connection"""

    postgres_user: str
    postgres_password: str
    postgres_database: str
    postgres_server: str
    postgres_port: str

    @property
    def postgres_uri(self) -> str:
        return PostgresDsn.build(
            scheme="postgresql",
            user=self.postgres_user,
            password=self.postgres_password,
            host=self.postgres_server,
            path=f"/{self.postgres_database}",
            port=self.postgres_port,
        )


class Settings(BaseSettings):
    uvicorn: UvicornSettings
    db_connection: DatabaseConnectionSettings
    api_config: ApiConfigSettings
    logging: LoggingConfigSettings


def load_from_yaml() -> Any:
    with open("appsettings.yaml") as file:
        config = yaml.safe_load(file)
    return config


def db_link(
        db: str,
        user: str,
        password: str,
        database: str,
        server: str = "db",
        port: str = 5432,
) -> str:
    link = f"{db}://{user}:{password}@{server}:{port}/{database}"
    return link


@lru_cache()
def get_settings() -> Settings:
    yaml_config = load_from_yaml()
    settings = Settings(**yaml_config)
    return settings
