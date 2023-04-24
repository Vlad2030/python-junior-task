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
    allowed_types: PetsType = PetsTypeModel.type_list
    return True if type in allowed_types else False


@router.post(
    path="/",
    status_code=HTTP_201_CREATED,
    summary="Create a pet",
    description="Creating a pet ¯\_(ツ)_/¯",
    response_model=PetsPostResponse,
)
async def pet_create(
        name: PetsName,
        age: PetsAge,
        type: PetsType,
) -> PetsPostResponse:
    if not check_pet_type(type=type):
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND,
            detail="Type doesn't exists",
        )
    
    return {
        "id": ...,
        "name": name,
        "age": age,
        "type": type,
        "created_at": ...
    }



@router.get(
    path="/",
    status_code=HTTP_200_OK,
    summary="",
    description="",
    response_model=PetsGetResponse
)
async def pets_list(limit: PetsLimit = 20) -> JSONResponse:
    ...

    return {
        "count": ...,
        "items": ...,
    }


@router.delete(
    path="/",
    status_code=HTTP_200_OK,
    summary="",
    description="",
    response_model=PetsDeleteResponse
)
async def pets_delete(ids: PetsIds) -> JSONResponse:
    ...
    errors: Dict[str, None] = []

    return {
        "deleted": ...,
        "errors": None if not errors else errors
    }