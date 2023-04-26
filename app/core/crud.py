from sqlalchemy.orm import Session

from core.database import Database
from orm.pets import Pets
from schemas.responses import (PetsDeleteResponse, PetsGetResponse,
                               PetsPostResponse)


class Pet:
    def __init__(self, database: Session) -> None:
        self.database: Session = database

    def create(self, pet: PetsPostResponse):
        database_pet = Pets(**pet.dict())
        self.database.add(database_pet)
        self.database.commit()
        self.database.refresh(database_pet)
        return database_pet

    def get_all(self, limit: int) -> list:
        return self.database.query(Pets).limit(limit).all()

    def delete(self, ids: list):
        deleted = 0
        errors = []
        for id in ids:
            pet = self.database.query(Pets).filter(PetsPostResponse.id==id).first()
        if not pet:
            return errors.append({"id": id, "error": "Pet with the matching ID was not found."})
        
        self.database.query(Pets).filter_by(id=id).delete()
        self.database.commit()
        return DeletePostResponse(detail="Post Deleted")
