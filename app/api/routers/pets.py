from typing import Dict, List, Union

from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from starlette import status
from starlette.responses import JSONResponse

from schemas.requests import Pets

router = APIRouter()

@router.post(
    path="/",
    status_code=status.HTTP_201_CREATED,
    summary="",
    description="",
    )
async def pet_create(
        name: str,
        age: int,
        type: str,
) -> JSONResponse:
    if type not in Pets.types:
        raise HTTPException(
            status_code=404,
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
    status_code=status.HTTP_200_OK,
)
async def pets_list(limit: int = 20) -> JSONResponse:
    ...

    return {
        "count": ...,
        "items": ...,
    }


@router.delete(
    path="/",
    status_code=status.HTTP_200_OK,
)
async def pets_delete(ids: List[int]) -> JSONResponse:
    ...
    errors: Dict[str, None] = []

    return {
        "deleted": ...,
        "errors": None if not errors else errors
    }