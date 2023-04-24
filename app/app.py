from fastapi import FastAPI, Response
from fastapi.exceptions import RequestValidationError
from loguru import logger
from starlette import status
from starlette.responses import JSONResponse

from config.settings import get_settings
from core.logger import setup_logger
from core.middleware.cors import setup_cors_middleware
from routers.api_routes import router
#from schemas import ApplicationResponse


def create_application() -> FastAPI:
    settings = get_settings()

    application = FastAPI(
        title=settings.api_config.title,
        description=settings.api_config.description,
        version=settings.api_config.version,
        docs_url=settings.api_config.docs_url,
    )
    application.debug = settings.api_config.debug
    setup_cors_middleware(app=application)
    application.include_router(router, prefix="/posts")

    @application.on_event("startup")
    async def startup() -> None:
        return logger.info("Application startup")

    @application.on_event("shutdown")
    async def shutdown() -> None:
        return logger.warning("Application shutdown")

    @application.get(path="/", status_code=status.HTTP_200_OK)
    async def healthcheck() -> Response:
        return {
            "ok": True,
            "result": True,
        }

    return application


app = create_application()