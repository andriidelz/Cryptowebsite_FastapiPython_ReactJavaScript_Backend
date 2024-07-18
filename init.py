from backend.http_client import CMCHTTPClient
from backend.config import settings

cmc_client = CMCHTTPClient(
    base_url="https://pro-api.coinmarketcap.com",
    api_key=settings.CMC_API_KEY
)
