class BaseError(Exception):
    CODE: str = "error"
    MESSAGE: str = "Что-то пошло не так"
    STATUS: int = 400

    def __init__(
        self,
        *,
        code: str | None = None,
        message: str | None = None,
        status: int | None = None
    ) -> None:
        self.code = code or self.CODE
        self.message = message or self.MESSAGE
        self.status = status or self.STATUS

    def __str__(
        self
    ) -> str:
        return f"[{self.code}, HTTP/{self.status}] {self.message}"


class NotFoundError(BaseError):
    CODE = "not-found"
    MESSAGE = "Not found"
    STATUS = 404


class UnexpectedError(BaseError):
    STATUS = 500

    def __init__(
        self,
        original: Exception
    ) -> None:
        super().__init__()
        self.original = original


class ValidationError(BaseError):
    CODE = "validation"
    MESSAGE = "Ошибка валидации данных"

    def __init__(
        self,
        message: str | None = None
    ) -> None:
        super().__init__(message=message)
