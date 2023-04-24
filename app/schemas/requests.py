from typing import List, Union

from pydantic import BaseModel


class PetsName(BaseModel):
    name: str


class PetsAge(BaseModel):
    age: int


class PetsType(BaseModel):
    cat: str
    dog: str


class PetsLimit(BaseModel):
    limit: int


class PetsIds(BaseModel):
    ids: Union[int, List[int]]


class PetsPostRequest(BaseModel): ...


class PetsGetRequest(BaseModel): ...


class PetsDeleteRequest(BaseModel): ...