from database.models import Pets
from schemas.responses import (PetsDeleteResponse, PetsGetResponse,
                               PetsPostResponse)
from sqlalchemy.orm import Session


class Pet:
    def __init__(self, database: Session) -> None:
        self.database: Session = database


    def create(self, pet: PetsPostResponse) -> dict:
        database_pet = Pets(**pet.dict())
        self.database.add(database_pet)
        self.database.commit()
        self.database.refresh(database_pet)
        return database_pet


    def get_all(self, pet_limit: int) -> list:
        return self.database.query(Pets).limit(pet_limit).all()


    def delete(self, ids: list) -> dict:
        deleted = 0
        errors = []

        for id in ids:
            pet = self.database.query(Pets).filter(PetsPostResponse.id==id).first()

            if not pet:
                return errors.append({
                        "id": id,
                        "error": "Pet with the matching ID was not found.",
                    },
                )

            self.database.delete(pet)
            deleted += 1

        self.database.commit()
        return deleted, errors