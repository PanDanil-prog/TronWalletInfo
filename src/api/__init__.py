from fastapi import APIRouter

from . import (
    request_wallet,
    receive_requests
)


router = APIRouter()


router.include_router(
    request_wallet.router,
    prefix="/wallet"
)


router.include_router(
    receive_requests.router,
    prefix="/wallet-requests"
)
