from config.settings import DatabaseConnectionSettings, db_link, get_settings
from databases import Database as Databases
from sqlalchemy import MetaData, create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker


class Database:
    def __init__(self) -> None:
        conf = get_settings().db_connection
        self.database_url = db_link(db="postgresql+psycopg2",
                                    user=conf.postgres_user,
                                    password=conf.postgres_password,
                                    database=conf.postgres_database,
                                    server=conf.postgres_server,
                                    port=conf.postgres_port)
        self.database = Databases(self.database_url)
        self.metadata = MetaData()
        self.engine: Engine = create_engine(self.database_url)
        self.session_local: sessionmaker = scoped_session(sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=self.engine,
        ))

    def base(self) -> DeclarativeMeta:
        return declarative_base()

    def get(self) -> None:
        database = self.session_local()
        try:
            yield database
        finally:
            database.close()

    def create_all(self, engine: Engine) -> None:
        return self.metadata.create_all(engine)

    def drop_all(self, engine: Engine) -> None:
        return self.metadata.drop_all(engine)


database = Database()
Base = database.base()
engine = database.engine
