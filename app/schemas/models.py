from typing import List

from pydantic import BaseModel

from schemas.requests import PetsType


class PetsTypeModel(BaseModel):
    dog: str = "dog"
    cat: str = "cat"
    type_list: List[PetsType] = [dog, cat]
