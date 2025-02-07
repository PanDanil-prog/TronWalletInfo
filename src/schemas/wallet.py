from .base import BaseModel


class WalletBase(BaseModel):

    class Config:
        fields = dict(
            address=dict(
                title="Адрес кошелька в сети TRON",
                example='TMqbtDcVfsQtbHLaEp5xAZytdb88joUA9z'
            ),
            bandwidth=dict(
                title=""
            ),
            energy=dict(
                title=""
            ),
            balance_trx=dict(
                title=""
            )
        )