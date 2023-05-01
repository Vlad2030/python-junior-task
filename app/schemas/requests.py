from typing import List

from pydantic import BaseModel


class PetsPostRequest(BaseModel):
    name: str = "boy"
    age: int = 7
    type: str = "dog"


class PetsGetRequest(BaseModel):
    limit: int = 20


class PetsDeleteRequest(BaseModel):
    ids: List[int] = [1, 2, 3]
