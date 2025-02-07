import pytest
import sqlalchemy as sa

from models.tron_wallet import TronWalletRequests


@pytest.mark.asyncio
async def test_insert_wallet_request(test_db_session):
    async with test_db_session as conn:
        q = sa.insert(TronWalletRequests).values(address="TCQPAt3swdNMadK4DcbzGNnA146D5uQteZ")
        await conn.execute(q)

        q = sa.select(TronWalletRequests).where(TronWalletRequests.c.address == "TCQPAt3swdNMadK4DcbzGNnA146D5uQteZ")
        result = await conn.execute(q)
        row = result.fetchone()

    assert row is not None
    assert row.address == "TCQPAt3swdNMadK4DcbzGNnA146D5uQteZ"
