from datetime import datetime

from core.database import Base, engine
from sqlalchemy import Column, DateTime, Integer, String


class Pets(Base):
    __tablename__ = "pets"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(length=50))
    age = Column(Integer)
    type = Column(String(length=3))
    created_at = Column(DateTime, default=datetime.now)
