from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.engine import Engine

from core.database import Database

database = Database()
Base = database.db_base()
engine = database.connect()

class Pets(Base):
    __tablename__ = "pets"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(length=50))
    age = Column(Integer)
    type = Column(String(length=3))
    created_at = Column(DateTime)

    Base.metadata.create_all(bind=engine)
