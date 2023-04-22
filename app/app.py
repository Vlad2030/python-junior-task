from config.settings import get_settings
from core.logger import setup_logger
from core.middleware.cors import setup_cors_middleware
from fastapi import FastAPI, Response
from fastapi.exceptions import RequestValidationError
from loguru import logger
from routers.api_routes import router
from schemas import ApplicationResponse
from starlette import status
from starlette.responses import JSONResponse


def create_application() -> FastAPI:
    settings = get_settings()

    app = FastAPI(
        title=settings.api_config.title,
        description=settings.api_config.description,
        debug=settings.api_config.debug,
        version=settings.api_config.version,
        docs_url=settings.api_config.docs_url,
    )
    setup_cors_middleware(app=app)
    app.include_router(router, prefix="/posts")

    @app.on_event("startup")
    async def startup() -> None:
        return logger.info("Application startup")

    @app.on_event("shutdown")
    async def shutdown() -> None:
        return logger.warning("Application shutdown")

    @app.get(path="/", status_code=status.HTTP_200_OK)
    async def healthcheck() -> Response:
        return {
            "ok": True,
            "result": True,
        }

    return app


app = create_application()