from core.crud import Session
from core.database import Database
from fastapi.params import Depends as DependsType

db = Database()

class SessionMixin:
    def __init__(self) -> None:
        self._session: Session = db.get()

    def session(self) -> Session:
        if isinstance(self._session, DependsType):
            return next(db.get())
        return self._session