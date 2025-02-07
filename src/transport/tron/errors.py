from errors.base import BaseError


class TronError(BaseError):
    CODE: int = -1
    MESSAGE: str = "Что-то пошло не так"

    def __init__(
        self,
        /,
        code: int | None = None,
        message: str | None = None,
        status: int | None = None
    ) -> None:
        self.code = code if code is not None else self.CODE
        self.message = message or self.MESSAGE
        self.status = status or self.STATUS

    def __str__(self) -> str:
        return f"Tron error: [{self.code}] {self.message}"
