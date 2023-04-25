from datetime import datetime
from typing import List

from ormar import Boolean, DateTime, Integer, Model, String

from schemas.models import PetsTypeModel


class PetsPostResponse(Model):
    id: int = Integer(minimum=1)
    name: str = String(max_length=50, min_length=1)
    age: int = Integer(minimum=1, maximum=99)
    type: str = String(max_length=50, min_length=1)
    created_at: datetime = DateTime()


class PetsGetResponse(Model):
    count: int = Integer(minimum=1)
    items: List[PetsPostResponse]


class PetsGetListResponse(Model):
    items: PetsPostResponse


class PetsDeleteListResponce(Model):
    id: int = Integer()
    error: str = String(max_length=150)


class PetsDeleteResponse(Model):
    deleted: int = Integer()
    errors: List[PetsDeleteListResponce]


class HeathStatusCheckResonce(Model):
    ok: bool = Boolean()