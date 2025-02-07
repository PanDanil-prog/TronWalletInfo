from logging import getLogger
from logging.config import dictConfig

from fastapi import FastAPI
from fastapi.responses import UJSONResponse

from conf import (
    settings,
    LOGGING
)

from middlewares import setup_middlewares

import api


dictConfig(LOGGING)
logger = getLogger("base")

app = FastAPI(
    title="Tron Wallet Info",
    default_response_class=UJSONResponse,
    redoc_url=f"{settings.URL}/redoc",
    docs_url=f"{settings.URL}/docs",
    openapi_url=f"{settings.URL}/openapi.json"
)

app.openapi_version = "3.0.3"


@app.on_event("startup")
async def startup():
    logger.info("startup")


@app.on_event("shutdown")
async def shutdown():
    logger.warning("shutdown")


app.include_router(
    api.router,
    prefix=settings.URL
)

setup_middlewares(app)
