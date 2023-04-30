from config.settings import get_settings
from core.logger import setup_logger
from core.middleware.cors import setup_cors_middleware
from fastapi import FastAPI, Response
from loguru import logger
from routers.api_routes import router
from schemas.responses import HeathStatusCheckResponce
from starlette import status


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
    application.include_router(router=router, tags=["pets"])

    @application.on_event("startup")
    async def startup() -> None:
        return logger.info("Application startup")

    @application.on_event("shutdown")
    async def shutdown() -> None:
        return logger.warning("Application shutdown")

    @application.get(
        path="/",
        status_code=status.HTTP_200_OK,
        summary="Check health status",
        description="Check health status (´♡‿♡`)",
        response_model=HeathStatusCheckResponce,
    )
    async def healthcheck() -> Response:
        return {"ok": True}

    return application


app = create_application()
