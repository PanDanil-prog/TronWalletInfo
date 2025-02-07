
from ..http import HttpTransport

from .session import TronSession


class TronGridAPITransport(HttpTransport):

    def __init__(
            self,
            url: str,
            api_key: str,
            timeout: float,
            debug: bool = False,
            insecure: bool = False
    ) -> None:

        super().__init__(
            timeout=timeout,
            debug=debug,
            insecure=insecure
        )

        self.url = url

        self.headers = {
            "Authorization": f"Bearer {api_key}"
        }

    def session(
        self,
        /,
        **kwargs,
    ) -> TronSession:
        return super().session(
            url=self.url,
            headers=self.headers,
            skip_auto_headers=["user-agent"],
            **kwargs
        )

    class Session(TronSession):
        pass
