from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    ENVIRONMENT: str = "DEV"

    # Точка монтирования API
    URL: str = "/api"
    # API_DOMAIN: str

    # Подключение к БД
    DB_DSN: str = "postgresql+asyncpg://tron_user:tron_pass@db:5432/tron_db"
    DB_POOL_TIMEOUT: float = 5.0
    DB_POOL_SIZE: int = 10
    DB_POOL_RECYCLE: float = 300

    # TRON
    TRON_URL: str = "https://api.trongrid.io/v1/"
    TRON_API_KEY: str = "bb0cfa0a-1a33-4588-ba4b-ef4db0275df9"
    TRON_DEBUG: bool = False
    TRON_TIMEOUT: float = 5.0
    TRON_INSECURE: bool = False

    # HTTP-транспорт
    TRANSPORT_HTTP_TIMEOUT: float = 5.0