from datetime import datetime
from typing import List

from pydantic import BaseModel


class PetsPost(BaseModel):
    name: str
    age: int
    type: str


class PetsPostResponse(PetsPost):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


class PetsGetResponse(BaseModel):
    count: int 
    items: List[PetsPostResponse]


class PetsGetListResponse(BaseModel):
    items: PetsPostResponse


class PetsDeleteListResponce(BaseModel):
    id: int
    error: str


class PetsDeleteResponse(BaseModel):
    deleted: int
    errors: List[PetsDeleteListResponce]


class HeathStatusCheckResponce(BaseModel):
    ok: bool
