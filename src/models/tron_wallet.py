import sqlalchemy as sa

from .meta import metadata


TronWalletRequests = sa.Table(
    "tron_wallet_requests", metadata,
    sa.Column("id", sa.Integer, sa.Identity(), primary_key=True),
    sa.Column("address", sa.Text, nullable=False)
)
