from datetime import datetime

from pydantic import BaseModel


class PetsPostResponse(BaseModel):
    id: int = 1
    name: str = "boy"
    age: int = 7
    type: str = "dog"
    created_at: datetime


class PetsGetResponse(BaseModel):
    count: int = 2
    items: list


class PetsDeleteListResponce(BaseModel):
    id: int = 1
    error: str = "Pet with the matching ID was not found."


class PetsDeleteResponse(BaseModel):
    deleted: int = 2
    errors: list | None


class HeathStatusCheckResponce(BaseModel):
    ok: bool = True
