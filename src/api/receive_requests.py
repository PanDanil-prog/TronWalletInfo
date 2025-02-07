import sqlalchemy as sa

from fastapi import (
    APIRouter,
    Depends
)

from database import db

from depends.scroll import ScrollDepend, Scroll

from .schemas import WalletRequests, WalletRequest
from models.tron_wallet import TronWalletRequests


router = APIRouter()


@router.get(
    "/",
    summary=WalletRequests.Config.title,
    response_model=WalletRequests
)
async def handler(
    scroll: Scroll = Depends(
            ScrollDepend([])
        )
):
    q = sa.select(TronWalletRequests)

    q = scroll.apply(q)

    async with db.begin() as conn:
        items = [
            WalletRequest(
                id=row.id,
                address=row.address
            )
            async for row in await conn.stream(q)
        ]

    return WalletRequests(items=items)



