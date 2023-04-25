from config.settings import get_settings
from databases import Database
from sqlalchemy import MetaData, create_engine
from sqlalchemy.engine import Engine


class Database:
    def __init__(self) -> None:
        self.config: str = get_settings().db_connection
        self.database_url: str = self.config.postgres_uri()
        self.database = Database(self.database_url)
        self.metadata = MetaData()

    def connect(self) -> Engine:
        return create_engine(self.database_url)

    def create_all(self, engine: Engine) -> None:
        return self.metadata.create_all(engine)

    def drop_all(self, engine: Engine) -> None:
        return self.metadata.drop_all(engine)
