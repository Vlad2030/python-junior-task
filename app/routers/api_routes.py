from fastapi import APIRouter

from routers.routes import pets


def create_api_router() -> APIRouter:
    api_router = APIRouter()
    api_router.include_router(pets.router, tags=["pets"])

    return api_router


router = create_api_router()
