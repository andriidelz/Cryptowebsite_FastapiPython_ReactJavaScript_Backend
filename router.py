from fastapi import APIRouter
from backend.init import cmc_client

router = APIRouter(
    prefix="/currencies"
)


@router.get("")
async def get_cryptocurrencies():
    return await cmc_client.get_listings()


@router.get("/{currency_id}")
async def get_cryptocurrency(currency_id: int):
    return await cmc_client.get_currency(currency_id)
