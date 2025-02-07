import aiohttp


class TransportBaseError(Exception):
    pass


class TransportServerError(TransportBaseError):

    def __init__(
        self,
        response: aiohttp.ClientResponse
    ) -> None:
        super().__init__(
            f"Transport server error: HTTP/{response.status}"
        )
        self.status = response.status
        self.response = response


class TransportClientError(TransportBaseError):

    def __init__(
        self,
        response: aiohttp.ClientResponse
    ) -> None:
        super().__init__(
            f"Transport client error, HTTP/{response.status}"
        )
        self.status = response.status
        self.response = response


class TransportTimeoutError(TransportBaseError):

    def __init__(
        self
    ) -> None:
        super().__init__("Transport timeout")
