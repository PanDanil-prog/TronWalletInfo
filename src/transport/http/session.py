import aiohttp

from common import json

from .errors import (
    TransportClientError,
    TransportServerError,
    TransportTimeoutError
)


class HttpSession:

    def __init__(
        self,
        /,
        insecure: bool = False,
        **kwargs,
    ) -> None:
        self._kwargs = kwargs
        self._session: aiohttp.ClientSession | None = None
        # Небезопасный SSL
        self.ssl = False if insecure else None

    async def prepare(
        self,
        session: aiohttp.ClientSession
    ) -> None:
        pass

    async def __aenter__(self):
        if not self._session:
            self._session = aiohttp.ClientSession(
                json_serialize=json.dumps,
                **self._kwargs,
            )
            await self.prepare(self._session)
        return self

    async def __aexit__(self, exc_type, exc, tb):
        if self._session:
            await self._session.close()
            self._session = None

    async def request(
        self,
        method: str,
        url: str,
        **kwargs,
    ) -> aiohttp.ClientResponse:

        # Без сессии мы ничего не сделаем
        assert self._session

        # Дополнительные параметры
        params = {
            "ssl": self.ssl
        } | kwargs

        # Пробуем обработать запрос
        try:
            resp = await self._session.request(method, url, **params)
        except aiohttp.ServerTimeoutError:
            raise TransportTimeoutError

        # Ошибка сервера
        if any((
            resp.status > 500,
            resp.status < 200
        )):
            raise TransportServerError(resp)

        # Ошибка клиента
        if all((
            resp.status >= 300,
            resp.status <= 500
        )):
            raise TransportClientError(resp)

        # Все ОК
        return resp

    def post(
        self,
        url: str,
        **kwargs,
    ):
        return self.request("POST", url, **kwargs)

    def get(
        self,
        url: str,
        **kwargs,
    ):
        return self.request("GET", url, **kwargs)

    def put(
        self,
        url: str,
        **kwargs,
    ):
        return self.request("PUT", url, **kwargs)

    def delete(
        self,
        url: str,
        **kwargs,
    ):
        return self.request("DELETE", url, **kwargs)

    def head(
        self,
        url: str,
        **kwargs,
    ):
        return self.request("HEAD", url, **kwargs)
