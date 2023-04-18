from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.settings import cors_settings


def setup_cors_middleware(app: FastAPI) -> None:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=cors_settings.ALLOW_ORIGINS,
        allow_credentials=True,
        allow_methods=["GET", "POST", "DELETE"],
        allow_headers=["*"],
    )
