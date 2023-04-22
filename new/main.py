import uvicorn
from loguru import logger

from config.settings import get_settings

settings = get_settings()


def main() -> None:
#    logger.info(
#        f"Starting application. Uvicorn running on http(s):"
#        f"//{settings.uvicorn.host}:{settings.uvicorn.port} "
#    )
    #logger.info(f"Custom logging on: {logging_settings.CUSTOM_LOGGING_ON}")
    uvicorn.run(
        app="app:app",
        host=settings.uvicorn.host,
        port=settings.uvicorn.port,
        reload=settings.uvicorn.reload,
    )


if __name__ == "__main__":
    main()
