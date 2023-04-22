from sqlalchemy import create_engine
from config.settings import get_settings


class Database:
    def __init__(self) -> None:
        self.config: str = get_settings().db_connection
        self.database: str = self.config.postgres_uri

    def connect(self) -> None:
        return create_engine(self.database)