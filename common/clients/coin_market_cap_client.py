import logging
from typing import Dict, Any

import requests

from config.settings.base import COIN_MARKET_CAP_API_KEY


logger = logging.getLogger(__name__)


class CoinMarketCapClient:
    COIN_MARKET_CAP_API_URL = "https://sandbox-api.coinmarketcap.com"
    COIN_MARKET_CAP_API_GET_STATS_URL = (
        COIN_MARKET_CAP_API_URL + "/v1/blockchain/statistics/latest?symbol={symbol}"
    )  # symbol: BTC,LTC,ETH

    def get_blockchain_stats(self, symbol: str) -> Dict[str, Any]:
        headers = {
            "Accepts": "application/json",
            "X-CMC_PRO_API_KEY": COIN_MARKET_CAP_API_KEY
        }
        url = self.COIN_MARKET_CAP_API_GET_STATS_URL.format(symbol=symbol)
        response = requests.get(url=url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            logger.error(
                "CoinMarketCap get {} stats api error. Status code: {}. Response text: {}.",
                symbol,
                response.status_code,
                response.text,
            )
