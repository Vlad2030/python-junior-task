from typing import List

from ormar import JSON, DateTime, Integer, Model, String

from schemas.models import PetsTypeModel


class PetsPostResponse(Model):
    id: int = Integer()
    name: str = String(max_length=50, min_length=1)
    age: int = Integer(minimum=1, maximum=99)
    type: PetsTypeModel
    created_at: str = DateTime()


class PetsGetResponse(Model):
    count: int = Integer()
    items: List[PetsPostResponse] = JSON(PetsPostResponse)


class PetsDeleteListResponce(Model):
    id: int = Integer()
    error: str = String()


class PetsDeleteResponse(Model):
    deleted: int = Integer()
    errors: List[PetsDeleteListResponce] = JSON(PetsDeleteListResponce)