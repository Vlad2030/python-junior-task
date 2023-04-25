from typing import List, Union

from pydantic import BaseModel


class PetsName(BaseModel):
    name: str


class PetsAge(BaseModel):
    age: int


class AllowedPetsTypes(BaseModel):
    cat: str = "cat"
    dog: str = "dog"


class PetsType(BaseModel):
    type: str


class PetsLimit(BaseModel):
    limit: List[int]


class PetsIds(BaseModel):
    ids: List[int]


class PetsPostRequest(BaseModel): ...


class PetsGetRequest(BaseModel): ...


class PetsDeleteRequest(BaseModel): ...