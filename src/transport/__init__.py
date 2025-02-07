from functools import cache

from conf import settings

from .tron import TronGridAPITransport


@cache
def get_tron_transport() -> TronGridAPITransport:

    return TronGridAPITransport(
        settings.TRON_URL,
        settings.TRON_API_KEY,
        timeout=settings.TRON_TIMEOUT,
        debug=settings.TRON_DEBUG,
        insecure=settings.TRON_INSECURE
    )


tron_transport = get_tron_transport()
