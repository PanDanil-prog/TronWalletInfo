import sqlalchemy as sa

from fastapi import (
    APIRouter,
    Body
)

from database import db

from providers import tron

from .schemas import (
    WalletGet,
    Wallet as WalletSchema
)
from models.tron_wallet import TronWalletRequests


router = APIRouter()


@router.post(
    "/",
    summary=WalletGet.Config.title,
    response_model=WalletSchema
)
async def handler(
    req: WalletGet = Body(...)
) -> WalletSchema:

    wallet_data = await tron.get_account_info(wallet_address=req.address)
    wallet_info = wallet_data['data'][0]

    async with db.begin() as conn:
        q = sa.insert(TronWalletRequests).values(
            address=req.address
        )

        await conn.execute(q)

    return WalletSchema(
        address=req.address,
        balance_trx=wallet_info.get("balance", 0),
        energy=wallet_info.get("energy", 0),
        bandwidth=wallet_info.get("bandwidth", 0)
    )
