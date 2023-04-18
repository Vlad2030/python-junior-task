import logging

from fastapi import FastAPI, Request, Response
from fastapi.exceptions import RequestValidationError
from starlette import status
from starlette.responses import JSONResponse

from config.settings import get_settings
from core.logger import setup_logger
from core.middleware.cors import setup_cors_middleware
from new.routers.api_routes import router
from schemas import ApplicationResponse

settings = get_settings()

app = FastAPI(
    title=settings.api_config.title,
    description=settings.api_config.description,
    debug=settings.api_config.debug,
    version=settings.api_config.version,
    docs_url=settings.api_config.docs_url,
)
setup_cors_middleware(app=app)


@app.on_event("startup")
async def startup_event() -> None:
    # setup logger
    logger = logging.getLogger("uvicorn.access")
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
    logger.addHandler(handler)
    app.state.logger = logger


@app.exception_handler(RequestValidationError)
@app.exception_handler(Exception)
async def exception_handler(request: Request, exc: Exception) -> JSONResponse:
    logger = request.app.state.logger
    logger.error(f"{exc}")
    return error_response(errors=str(exc), status_code=status.HTTP_400_BAD_REQUEST)


app.include_router(router=router, prefix="/posts")


@app.get(path="/", status_code=status.HTTP_200_OK)
async def healthcheck() -> Response:
    return {
        "ok": True,
        "result": True,
    }


app = create_application()