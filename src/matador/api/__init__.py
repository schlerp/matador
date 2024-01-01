import fastapi
from fastapi.applications import FastAPI

from matador.api.v1 import dataset


def setup_api() -> FastAPI:
    app = fastapi.FastAPI(
        title="Matador",
        description="A simple API for managing dataset metadata.",
        version="0.1.0",
    )
    app.include_router(dataset.router)
    return app
