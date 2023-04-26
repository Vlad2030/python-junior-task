from datetime import datetime
from typing import Dict, List, Union

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette.exceptions import HTTPException
from starlette.responses import JSONResponse
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_404_NOT_FOUND
from core.database import Database
from core.crud import Pet as PetCrud
from schemas.models import PetsTypeModel
from schemas.requests import PetsIds, PetsType
from schemas.responses import (PetsDeleteListResponce, PetsDeleteResponse,
                               PetsGetResponse, PetsPostResponse)


def get_engine() -> None:
    database = Database()
    engine = database.connect()
    session = database.session_local(engine=engine)
    return database.get()


router = APIRouter()


def check_pet_type(type: PetsTypeModel) -> bool:
    """### Check Pet Type

    Returns `True` if type matches.

    Else returns `False`.
    """
    allowed_types: PetsType = ["dog", "cat"]# PetsTypeModel.type_list
    return True if type in allowed_types else False


@router.post(
    path="/pets",
    status_code=HTTP_201_CREATED,
    summary="Create a pet",
    description="Creating a pet ¯\_(ツ)_/¯",
    response_model=PetsPostResponse,
)
async def pet_create(
        pet: PetsPostResponse,
        db: Session = Depends(),
) -> JSONResponse:
    """/pets POST Pet Create func

    Args:
        name (str): Pet name
        age (int): Pet age
        type (str): Pet type


    Raises:
        HTTPException: raise if type doesn't match or doesn't exist

        Example: {
            "detail": [
                {
                    "loc": [
                        "string",
                        0
                    ],
                    "msg": "string",
                    "type": "string"
                }
            ]
        }
        


    Returns:
        JSONResponse: JSON data of new pet

        Example: {
            "id": 1,
            "name": "string",
            "age": 99,
            "type": "string",
            "created_at": "2023-04-25T19:46:58.774Z"
        }
    """
    if not check_pet_type(type=type):
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND,
            detail="Type doesn't exists",
        )
    _session = Database().session_local
    _pet = PetCrud(database=...)
    
    return {
        "id": id,
        "name": ...,
        "age": ...,
        "type": type,
        "created_at": created_at
    }


@router.get(
    path="/pets",
    status_code=HTTP_200_OK,
    summary="Get all pets",
    description="Gettings all pets ( ͡° ͜ʖ ͡° )",
    response_model=PetsGetResponse
)
async def pets_list(limit: int = 20) -> JSONResponse:
    """/pets GET all pets list

    Args:
        limit (int, optional): Pet amount. Defaults to 20.


    Returns:
        JSONResponse: JSON data of all pets
    
        Example: {
            "count": 1,
            "items": [
                {
                    "id": 1,
                    "name": "string",
                    "age": 99,
                    "type": "string",
                    "created_at": "2023-04-25T19:50:43.399Z"
                }
            ]
        }
    """
    items: list = PetCrud(database=get_engine()).get_all()
    count: int = len(items)
    return {
        "count": count,
        "items": items,
    }


@router.delete(
    path="/pets",
    status_code=HTTP_200_OK,
    summary="Delete pets",
    description="Deleting pets by ID ( •_•)",
    response_model=PetsDeleteResponse
)
async def pets_delete(ids: PetsIds) -> JSONResponse:
    """ /pets DELETE pets by id

    Args:
        ids (list): list of pets id to delete

    Returns:
        JSONResponse: JSON data answer
    
        Example: {
            "deleted": 0,
            "errors": [
                {
                    "id": 0,
                    "error": "string"
                }
            ]
        }
    """
    ...
    errors: Dict[str, None] = []

    return {
        "deleted": ...,
        "errors": None if not errors else errors
    }
