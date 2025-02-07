from pydantic import BaseModel, Field

from schemas.wallet import WalletBase


class WalletGet(WalletBase):
    address: str = Field(..., min_length=34)

    class Config:
        title = "Получить информацию по кошельку в сети TRON"


class Wallet(WalletBase):
    address: str
    bandwidth: float
    energy: float
    balance_trx: float


class WalletRequest(WalletBase):
    id: int
    address: str


class WalletRequests(BaseModel):
    items: list[WalletRequest]

    class Config:
        title = "Получить информацию о запросах кошельков"
