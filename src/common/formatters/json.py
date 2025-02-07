import json
import logging

from uuid import UUID
from datetime import datetime, date
from traceback import TracebackException


class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        if isinstance(obj, date):
            return obj.isoformat()
        if isinstance(obj, UUID):
            return str(obj)
        if isinstance(obj, Exception):
            tb = TracebackException.from_exception(obj)
            data = dict(
                type=type(obj).__name__,
                message=str(obj),
                traceback="".join(tb.format())
            )
            return data
        return json.JSONEncoder.default(self, obj)


class JSONFormatter(logging.Formatter):

    def format(
        self,
        record: logging.LogRecord
    ) -> str:

        # Дата / время
        ts = datetime.utcfromtimestamp(record.created)

        # Сообщение
        if isinstance(record.msg, str):
            msg = record.msg % record.args
        else:
            msg = record.msg

        # Формируем запись
        data: dict[str, object] = {
            "timestamp": ts.isoformat(),
            "level": record.levelname,
            "message": msg
        }

        # Возвращем ответ
        return json.dumps(
            data,
            cls=JSONEncoder,
            ensure_ascii=True
        )
