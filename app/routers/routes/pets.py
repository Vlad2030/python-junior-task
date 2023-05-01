from core.crud import Pet as PetCrud
from core.database import Database
from core.exceptions import (HTTP_200_OK, HTTP_201_CREATED, PETS_ID_NOT_FOUND,
                             PetsNullDeleteException, PetsTypeException)
from fastapi import APIRouter
from schemas.models import PetsTypeModel
from schemas.requests import PetsIds, PetsType
from schemas.responses import (PetsDeleteResponse, PetsGetResponse, PetsPost,
                               PetsPostResponse)
from starlette.exceptions import HTTPException
from starlette.responses import JSONResponse

router = APIRouter()


def check_pet_type(type: PetsTypeModel) -> bool:
    """### Check Pet Type

    Returns `True` if type matches.

    Else returns `False`.
    """
    allowed_types: PetsType = ["dog", "cat"]
    return True if type in allowed_types else False


@router.post(
    path="/pets",
    status_code=HTTP_201_CREATED,
    summary="Create a pet",
    description="Creating a pet ¯\_(ツ)_/¯",
    response_model=PetsPostResponse,
)
async def pet_create(pet: PetsPost) -> JSONResponse:
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
        raise PetsTypeException

    db = Database().session_local
    crud = PetCrud(database=db)
    response: PetsPostResponse = crud.create(pet=pet)
    return {
        "id": response.id,
        "name": response.name,
        "age": response.age,
        "type": response.type,
        "created_at": response.created_at,
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
    db = Database().session_local
    crud = PetCrud(database=db)
    response: list[PetsPostResponse] = crud.get_all(pet_limit=limit)
    return {
        "count": len(response),
        "items": response,
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
    db = Database().session_local
    crud = PetCrud(database=db)
    
    deleted: int = 0
    errors: list = []

    for id in ids:
        pet = crud.get_one_by_id(id=id)

        if not pet:
            errors.append({
                    "id": id,
                    "error": PETS_ID_NOT_FOUND,
                },
            )
            continue

        crud.delete(pet_id=id)
        deleted +=1

    if deleted < 1:
        raise PetsNullDeleteException

    return {
        "deleted": deleted,
        "errors": None if not errors else errors,
    }
