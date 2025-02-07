import pytest
import sqlalchemy as sa

from database import db

from models.tron_wallet import TronWalletRequests


@pytest.mark.asyncio
async def test_insert_wallet_request():
    async with db.begin() as conn:
        q_ins = sa.insert(
            TronWalletRequests
        ).values(
            address="TCQPAt3swdNMadK4DcbzGNnA146D5uQteZ"
        ).returning(TronWalletRequests.c.id)
        row_id = await conn.scalar(q_ins)

        q_get = sa.select(
            TronWalletRequests
        ).where(
            TronWalletRequests.c.id == row_id)
        result = await conn.execute(q_get)
        row = result.fetchone()

        q_del = sa.delete(TronWalletRequests).where(TronWalletRequests.c.id == row.id)
        await conn.execute(q_del)


    assert row is not None
    assert row.address == "TCQPAt3swdNMadK4DcbzGNnA146D5uQteZ"
