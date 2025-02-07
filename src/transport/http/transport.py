import io
import aiohttp

from logging import getLogger
from time import monotonic

from conf import settings

from .session import HttpSession


logger = getLogger("base")


def dump_body(
    body: bytes
) -> str:
    try:
        text = body.decode("utf-8")
    except UnicodeDecodeError:
        text = "bytes([{body}])".format(
            body=",".join(f"0x{b:X}" for b in body),
        )
    except Exception:
        text = "(dump body failed)"
    return text


class HttpTransport:

    def __init__(
        self,
        /,
        timeout: float = settings.TRANSPORT_HTTP_TIMEOUT,
        debug: bool = False,
        insecure: bool = False
    ) -> None:

        # Таймаут выполнения запросов
        self.timeout = aiohttp.ClientTimeout(total=timeout)

        # Небезопасный SSL
        self.insecure = insecure

        # Отладочный режим
        self.debug = debug
        self.trace_configs: list[aiohttp.TraceConfig] = []
        if self.debug:
            trace = aiohttp.TraceConfig()
            trace.on_request_start.append(self.on_request_start)
            trace.on_request_end.append(self.on_request_end)
            trace.on_request_chunk_sent.append(self.on_request_chunk_sent)
            self.trace_configs.append(trace)

    async def on_request_start(
        self,
        session,
        ctx,
        params
    ) -> None:
        ctx.start = monotonic()
        ctx.body = io.BytesIO()

    async def on_request_chunk_sent(
        self,
        session,
        ctx,
        params
    ) -> None:
        if isinstance(params.chunk, bytes):
            ctx.body.write(params.chunk)

    async def on_request_end(
        self,
        session,
        ctx,
        params
    ) -> None:
        request = params.response.request_info

        # Тело запроса
        send = dump_body(
            ctx.body.getvalue()
        )

        # Тело ответа
        recv = dump_body(
            await params.response.read()
        )

        # Журнал
        logger.debug({
            "message": "HTTP-transport trace",
            "transport": type(self).__name__,
            "request": {
                "method": request.method,
                "url": str(request.url),
                "headers": dict(request.headers),
                "body": send
            },
            "response": {
                "status": params.response.status,
                "headers": dict(params.response.headers),
                "body": recv
            },
            "elapsed": monotonic() - ctx.start
        })

    def session(
        self,
        **kwargs,
    ) -> HttpSession:
        params = {
            "trace_configs": self.trace_configs,
            "timeout": self.timeout
        } | kwargs
        return self.Session(insecure=self.insecure, **params)

    class Session(HttpSession):
        pass
