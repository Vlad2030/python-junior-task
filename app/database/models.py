from datetime import datetime

from core.database import Base, engine
from sqlalchemy import Column, DateTime, Integer, String


class PetsDatabase(Base):
    __tablename__ = "pets"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(length=50))
    age = Column(Integer)
    type = Column(String())
    created_at = Column(DateTime, default=datetime.now)

Base.metadata.create_all(bind=engine)
