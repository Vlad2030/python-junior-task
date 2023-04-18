from api.api import router
from core.logger import setup_logger
from core.middleware import setup as setup_middleware
from core.settings import fastapi_settings, swagger_settings
from fastapi import FastAPI
from fastapi import Response
from loguru import logger
from schemas import ApplicationResponse
from starlette import status



def create_application() -> FastAPI:
    """
    Setup FastAPI application: middleware, exception handlers, jwt, logger.
    """

    application = FastAPI(
        title="test_task",
        description="API for test-task.",
        version="0.0.1",
        debug=fastapi_settings.DEBUG,
        docs_url=swagger_settings.DOCS_URL,
        redoc_url=swagger_settings.REDOC_URL,
        openapi_url=swagger_settings.OPENAPI_URL,
    )
    application.include_router(router)

    setup_middleware(application)
    setup_logger()

    @application.on_event("startup")
    async def startup() -> None:
        logger.info("Application startup")

    @application.on_event("shutdown")
    async def shutdown() -> None:
        logger.warning("Application shutdown")

    @application.get(path="/", status_code=status.HTTP_200_OK)
    async def healthcheck() -> Response:
        return {
            "ok": True,
            "result": True,
        }

    return application


app = create_application()
