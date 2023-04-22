from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine import Engine
from sqlalchemy import  (
    Column,
    Integer,
    String,
    DateTime,
)


Base = declarative_base()


class Pet(Base):
    __tablename__ = "pets"

    count = Column(Integer)
    #items = Enum
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)
    type = Column(String)
    created_at = Column(DateTime)

    def create_database(engine: Engine) -> None:
        return Base.metadata.create_all(bind=engine)