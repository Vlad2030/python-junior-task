import uvicorn
from loguru import logger

from core.settings import logging_settings, uvicorn_settings


def main() -> None:
    logger.info(
        f"Starting application. Uvicorn running on http(s):"
        f"//{uvicorn_settings.HOSTNAME}:{uvicorn_settings.PORT} "
    )
    logger.info(f"Custom logging on: {logging_settings.CUSTOM_LOGGING_ON}")
    uvicorn.run(
        app="app:app",
        host=uvicorn_settings.HOSTNAME,
        port=uvicorn_settings.PORT,
        reload=uvicorn_settings.RELOAD,
    )


if __name__ == "__main__":
    main()
