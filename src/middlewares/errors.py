from logging import getLogger
from uuid import uuid4

from fastapi import Request, Response
from fastapi.responses import UJSONResponse

import errors


logger = getLogger("base")


async def handler(
    request: Request,
    exc: Exception
) -> Response:

    # Генерируем номер ошибки
    ticket = uuid4().hex

    # Оформляем исключение
    if isinstance(exc, errors.BaseError):
        exc_ = exc
    else:
        exc_ = errors.UnexpectedError(exc)
    params = {
        "exception": exc,
        "ticket": ticket
    }

    # Журнал
    logger.error(params)

    # Отдаем ответ
    return UJSONResponse(
        status_code=exc_.status,
        content={
            "code": exc_.code,
            "message": exc_.message,
            "ticket": ticket
        }
    )
