from core.exceptions import PET_ID_NOT_FOUND
from database.models import PetsDatabase
from schemas.responses import (PetsDeleteResponse, PetsGetResponse,
                               PetsPostResponse)
from sqlalchemy.orm import Session


class CRUDPet:
    def __init__(self, database: Session) -> None:
        self.database: Session = database

    def create(self, pet: PetsPostResponse) -> PetsPostResponse:
        database_pet = PetsDatabase(**pet.dict())
        self.database.add(database_pet)
        self.database.commit()
        self.database.refresh(database_pet)
        return database_pet

    def get_all(self, pet_limit: int) -> PetsGetResponse:
        return (self.database.query(PetsDatabase)
                             .limit(pet_limit)
                             .all())

    def get_one_by_id(self, id: int) -> PetsPostResponse:
        return (self.database.query(PetsDatabase)
                             .filter_by(id=id)
                             .one())

    def delete_by_id(self, pet: int) -> None:
        pet = (self.database.query(PetsDatabase)
                            .filter(pet == id)
                            .first())
        self.database.delete(pet)
        self.database.commit()
        return pet

    def delete(self, pet: list[int]) -> PetsDeleteResponse:
        deleted: int = 0
        errors: list = []

        for id in pet.ids:    # .ids from PetsDeleteResponse schema
            db_pet = (self.database.query(PetsDatabase)
                                   .filter(PetsDatabase.id == id)
                                   .first())

            if not db_pet:
                errors.append(
                    {
                        "id": id,
                        "error": PET_ID_NOT_FOUND,
                    },
                )
                continue

            self.database.delete(db_pet)
            deleted += 1

        self.database.commit()
        return deleted, errors
