from config.settings import DatabaseConnectionSettings, db_link, get_settings
from databases import Database as Databases
from sqlalchemy import MetaData, create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import sessionmaker


class Database:
    def __init__(self) -> None:
        conf = get_settings().db_connection
        self.database_url = db_link(db="postgresql",
                                    user=conf.postgres_user,
                                    password=conf.postgres_password,
                                    database=conf.postgres_database,
                                    port=conf.postgres_port)
        self.database = Databases(self.database_url)
        self.metadata = MetaData()
        #self.connect: Engine = create_engine(self.database_url)

    def connect(self) -> Engine:
        yield create_engine(self.database_url)

    def session_local(self, engine: Engine) -> sessionmaker:
        return sessionmaker(autocommit=False, autoflush=False, bind=engine)

    def base(self) -> DeclarativeMeta:
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


database = Database()
Base = database.base()
engine = database.connect()
