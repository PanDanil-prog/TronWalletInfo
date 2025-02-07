from urllib.parse import urljoin

from common.json import loads

from transport.tron import TronGridAPITransport, TronSession


class TronProvider:

    def __init__(
        self,
        transport: TronGridAPITransport,
        /
    ) -> None:
        self.transport = transport

    def session(self) -> TronSession:
        return self.transport.session()

    async def get_account_info(
        self,
        wallet_address: str
    ) -> dict:
        """
        Получить информацию о кошельке TRON
        """

        async with self.session() as s:
            url = urljoin(s.url, f"accounts/{wallet_address}")
            resp = await s.get(url)
            data = await resp.text()

            data_dict = loads(data)

            if data_dict.get("data") == []:
                data_dict['data'] = [{
                    "address": wallet_address,
                    "balance": 0.0,
                    "bandwidth": 0.0,
                    "energy": 0.0,
                }]

            return data_dict
