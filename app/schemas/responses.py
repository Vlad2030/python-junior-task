from datetime import datetime
from typing import List, Dict

from pydantic import BaseModel


class PetsPost(BaseModel):
    name: str
    age: int
    type: str


class PetsPostResponse(PetsPost):
    id: int
    created_at: datetime


class PetsGetResponse(BaseModel):
    count: int 
    items: list


class PetsGetListResponse(BaseModel):
    items: PetsPostResponse


class PetsDeleteListResponce(BaseModel):
    id: int
    error: str


class PetsDeleteResponse(BaseModel):
    deleted: int
    errors: list


class HeathStatusCheckResponce(BaseModel):
    ok: bool
