from datetime import datetime
from typing import Dict, List, Union

from fastapi import APIRouter
from starlette.exceptions import HTTPException
from starlette.responses import JSONResponse
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_404_NOT_FOUND

from orm import pets
from schemas.models import PetsTypeModel
from schemas.requests import PetsAge, PetsIds, PetsLimit, PetsName, PetsType
from schemas.responses import (PetsDeleteListResponce, PetsDeleteResponse,
                               PetsGetResponse, PetsPostResponse)


router = APIRouter()


def check_pet_type(type: PetsTypeModel) -> bool:
    """### Check Pet Type

    Returns `True` if type matches.

    Else returns `False`.
    """
    allowed_types: PetsType = ["dog", "cat"]#PetsTypeModel.type_list
    return True if type in allowed_types else False


@router.post(
    path="/",
    status_code=HTTP_201_CREATED,
    summary="Create a pet",
    description="Creating a pet ¯\_(ツ)_/¯",
    response_model=PetsPostResponse,
)
async def pet_create(
        name: str,
        age: int,
        type: str,
) -> JSONResponse:
    if not check_pet_type(type=type):
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND,
            detail="Type doesn't exists",
        )
    id: int = 1
    created_at: datetime = datetime.now()
    
    return {
        "id": id,
        "name": name,
        "age": age,
        "type": type,
        "created_at": created_at
    }



@router.get(
    path="/",
    status_code=HTTP_200_OK,
    summary="Get all pets",
    description="Gettings all pets ( ͡° ͜ʖ ͡° )",
    response_model=PetsGetResponse
)
async def pets_list(limit: int = 20) -> JSONResponse:
    ...
    count = 1
    items = [limit, count]
    return {
        "count": count,
        "items": items,
    }


@router.delete(
    path="/",
    status_code=HTTP_200_OK,
    summary="Delete pets",
    description="Deleting pets by ID ( •_•)",
    response_model=PetsDeleteResponse
)
async def pets_delete(ids: PetsIds) -> JSONResponse:
    ...
    errors: Dict[str, None] = []

    return {
        "deleted": ...,
        "errors": None if not errors else errors
    }