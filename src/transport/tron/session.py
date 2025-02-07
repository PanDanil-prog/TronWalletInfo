import aiohttp

from transport.http import HttpSession, TransportClientError

from . import errors


class TronSession(HttpSession):

    def __init__(
        self,
        /,
        url: str,
        **kwargs
    ) -> None:
        super().__init__(**kwargs)
        self.url = url

    async def request(
        self,
        method: str,
        url: str,
        /,
        **kwargs,
    ) -> aiohttp.ClientResponse:

        try:

            # Выполняем запрос
            return await super().request(method, url, **kwargs)

        except TransportClientError as e:

            # Пробуем распарсить ошибку
            try:

                # Парсим ответ
                data = await e.response.json()
                print(data)
                code = int(data["statusCode"])
                message = data["error"]

                # Неизвестная ошибка
                raise errors.TronError(code=code, message=message)

            except errors.TronError:
                raise

            except Exception:
                pass

            # Прочие ошибки
            raise
