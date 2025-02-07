from fastapi import FastAPI, HTTPException
from starlette.middleware.errors import ServerErrorMiddleware

from . import errors


def setup_middlewares(
    app: FastAPI
) -> None:

    # Обработка ошибок
    app.add_middleware(ServerErrorMiddleware, handler=errors.handler)
    app.exception_handler(HTTPException)(errors.handler)
