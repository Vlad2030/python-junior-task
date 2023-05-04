from core.constants import (LIMIT_LESS_THAN_ZERO, PETS_NO_WERE_DELETED,
                            PETS_TYPE_DOESNT_EXIST)
from core.crud import CRUDPet
from core.database import Database
from fastapi import APIRouter
from schemas.models import PetsTypeModel
from schemas.requests import PetsDeleteRequest, PetsPostRequest
from schemas.responses import (PetsDeleteResponse, PetsGetResponse,
                               PetsPostResponse)
from starlette.exceptions import HTTPException
from starlette.responses import JSONResponse
from starlette.status import (HTTP_200_OK, HTTP_201_CREATED,
                              HTTP_400_BAD_REQUEST)

router = APIRouter()


def check_pet_type(type: PetsTypeModel) -> bool:
    """### Check Pet Type

    Returns `True` if type matches.

    Else returns `False`.
    """
    allowed_types = ["dog", "cat"]
    return True if type in allowed_types else False


@router.post(
    path="/pets",
    status_code=HTTP_201_CREATED,
    summary="Create a pet",
    description="Creating a pet ¯\_(ツ)_/¯",
    response_model=PetsPostResponse,
)
def pet_create(pet: PetsPostRequest) -> JSONResponse:
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
            "created_at": "2023-04-25T19:46:58.774"
        }
    """
    if not check_pet_type(type=pet.type):
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail=PETS_TYPE_DOESNT_EXIST,
        )

    db = Database().session_local
    crud = CRUDPet(database=db)
    response: PetsPostResponse = crud.create(pet=pet)
    return response


@router.get(
    path="/pets",
    status_code=HTTP_200_OK,
    summary="Get all pets",
    description="Gettings all pets ( ͡° ͜ʖ ͡° )",
    response_model=PetsGetResponse
)
def pets_list(limit: int = 20) -> JSONResponse:
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
    if limit < 0:
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail=LIMIT_LESS_THAN_ZERO,
        )

    db = Database().session_local
    crud = CRUDPet(database=db)
    items = crud.get_all(pet_limit=limit)
    return {
        "count": len(items),
        "items": items,
    }


@router.delete(
    path="/pets",
    status_code=HTTP_200_OK,
    summary="Delete pets",
    description="Deleting pets by ID ( •_•)",
    response_model=PetsDeleteResponse
)
async def pets_delete(ids: PetsDeleteRequest) -> JSONResponse:
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
    db = Database().session_local
    crud = CRUDPet(database=db)
    deleted, errors = crud.delete(pet=ids)
    if not deleted:
        raise HTTPException(
            status_code=HTTP_200_OK,
            detail=PETS_NO_WERE_DELETED,
        )

    return {
        "deleted": deleted,
        "errors": None if not errors else errors,
    }
