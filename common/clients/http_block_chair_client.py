import logging
from typing import Dict, Any

import requests


logger = logging.getLogger(__name__)


class BlockChairClient:
    BLOCK_CHAIR_API_URL = "https://api.blockchair.com/"
    BLOCK_CHAIR_API_GET_STATS_URL = BLOCK_CHAIR_API_URL + "{chain}/stats"  # chain: ethereum, bitcoin, etc.

    def get_blockchain_stats(self, chain: str) -> Dict[str, Any]:
        headers = {"Content-Type": "application/json;charset=utf-8"}
        url = self.BLOCK_CHAIR_API_GET_STATS_URL.format(chain=chain)
        response = requests.get(url=url, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            logger.error(
                "BlockChair get {} stats api error. Status code: {}. Response text: {}.",
                chain,
                response.status_code,
                response.text,
            )
