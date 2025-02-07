from functools import cache

from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncEngine
)

from conf import settings


@cache
def get_engine() -> AsyncEngine:
    return create_async_engine(
        settings.DB_DSN,
        pool_size=settings.DB_POOL_SIZE,
        pool_timeout=settings.DB_POOL_TIMEOUT,
        pool_recycle=settings.DB_POOL_RECYCLE,
        max_overflow=0,
        connect_args={
            "server_settings": {
                "application_name": "tron wallet",
                "client_encoding": "utf-8",
                "timezone": "utc",
                "jit": "off"
            }
        }
    )


db = get_engine()
