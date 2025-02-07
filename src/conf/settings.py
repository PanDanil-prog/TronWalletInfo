from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    ENVIRONMENT: str = "DEV"

    # Точка монтирования API
    URL: str = "/api"

    # Подключение к БД
    DB_DSN: str
    DB_POOL_TIMEOUT: float = 5.0
    DB_POOL_SIZE: int = 10
    DB_POOL_RECYCLE: float = 300

    # TRON
    TRON_URL: str = "https://api.trongrid.io/v1/"
    TRON_API_KEY: str
    TRON_DEBUG: bool = False
    TRON_TIMEOUT: float = 5.0
    TRON_INSECURE: bool = False

    # HTTP-транспорт
    TRANSPORT_HTTP_TIMEOUT: float = 5.0