import uvicorn
from loguru import logger

from config.settings import get_settings


def main() -> None:
    settings = get_settings()

    logger.info(
        f"Starting application. Uvicorn running on http(s):"
        f"//{settings.uvicorn.host}:{settings.uvicorn.port} "
    )
    logger.info(f"Custom logging on: {settings.logging.custom_log_level}")
    uvicorn.run(
        app="app:app",
        host=settings.uvicorn.host,
        port=settings.uvicorn.port,
        reload=settings.uvicorn.reload,
    )


if __name__ == "__main__":
    main()
