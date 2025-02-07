from functools import lru_cache
from .settings import Settings
from .logging import LOGGING  # noqa: F401


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()


__all__ = (
    "Settings",
    "settings",
    "LOGGING"
)
