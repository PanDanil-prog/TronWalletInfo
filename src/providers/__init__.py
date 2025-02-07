from functools import cache

from transport import tron_transport

from .tron import TronProvider


@cache
def get_tron_provider() -> TronProvider:
    return TronProvider(
        tron_transport
    )


tron = get_tron_provider()
