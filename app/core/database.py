from databases import Database as Databases
from sqlalchemy import MetaData, create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config.settings import DatabaseConnectionSettings, db_link, get_settings


class Database:
    def __init__(self) -> None:
        conf = get_settings().db_connection
        self.database_url = db_link(db="postgresql+psycopg2",
                                    user=conf.postgres_user,
                                    password=conf.postgres_password,
                                    database=conf.postgres_database,
                                    server=conf.postgres_server,
                                    port=conf.postgres_port)
        self.database = Databases("postgresql://localhost:5432")
        self.metadata = MetaData()

    def connect(self) -> Engine:
        return create_engine(self.database_url, pool_pre_ping=True)

    def session_local(self, engine: Engine) -> sessionmaker:
        return sessionmaker(autocommit=False, autoflush=False, bind=engine)

    def db_base(self) -> None:
        return declarative_base()

    def get(self) -> None:
        database = Database.session_local(
            engine=Database.connect()
        )
        yield database
        database.close()

    def create_all(self, engine: Engine) -> None:
        return self.metadata.create_all(engine)

    def drop_all(self, engine: Engine) -> None:
        return self.metadata.drop_all(engine)
