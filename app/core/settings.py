from os import path
from typing import Any, List, Tuple, cast

import orjson
from pydantic import BaseConfig
from pydantic import BaseSettings as PydanticBaseSettings
from pydantic import Field


class BaseSettings(PydanticBaseSettings):
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


class ApplicationSettings(BaseSettings):
    APP_URL: str = "http://localhost:80"

    @property
    def confirm_registration(self) -> str:
        return path.join(self.APP_URL, "register/email-confirmation")

    @property
    def restore_password(self) -> str:
        return path.join(self.APP_URL, "resetPassword")

    @property
    def change_password(self) -> str:
        return path.join(self.APP_URL, "changePassword")


application_settings = ApplicationSettings()


class DatabaseSettings(BaseSettings):
    RDS_DRIVER: str = "postgresql+asyncpg"
    RDS_USERNAME: str = "postgres"
    RDS_PASSWORD: str = "postgres"
    RDS_HOSTNAME: str = "database"
    RDS_PORT: str = "5432"
    RDS_DB_NAME: str = "postgres"

    @property
    def url(self) -> str:
        driver, user, password, host, port, name = (
            self.RDS_DRIVER,
            self.RDS_USERNAME,
            self.RDS_PASSWORD,
            self.RDS_HOSTNAME,
            self.RDS_PORT,
            self.RDS_DB_NAME,
        )
        return f"{driver}://{user}:{password}@{host}:{port}/{name}"


database_settings = DatabaseSettings()


class FastAPISettings(BaseSettings):
    DEBUG: bool = True


fastapi_settings = FastAPISettings()


class LoggingSettings(BaseSettings):
    LOGGING_LEVEL: str = "DEBUG"
    LOGGING_FILE_PATH: str = "logs/app.log"
    CUSTOM_LOGGING_ON: bool = False


logging_settings = LoggingSettings()


class UvicornSettings(BaseSettings):
    HOSTNAME: str = "0.0.0.0"
    PORT: int = 80
    RELOAD: bool = False


uvicorn_settings = UvicornSettings()


class SwaggerSettings(BaseSettings):
    DOCS_URL: str = "/docs"
    REDOC_URL: str = "/redoc"
    OPENAPI_URL: str = "/openapi.json"


swagger_settings = SwaggerSettings()

