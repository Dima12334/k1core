import logging
from datetime import datetime

from blocks.models import Block
from blocks.schemas import CreateBlockSchema
from common.clients.coin_market_cap_client import CoinMarketCapClient
from common.clients.http_block_chair_client import BlockChairClient
from common.models import Currency
from providers.models import Provider


logger = logging.getLogger(__name__)


def refresh_btc_latest_blocks_data():
    coin_market_cap_provider = Provider.objects.filter(name="CoinMarketCap").first()
    if not coin_market_cap_provider:
        logger.error("CoinMarketCap provider does not exists")
        return

    client = CoinMarketCapClient()

    currency = Currency.objects.filter(name__iexact="Bitcoin").first()
    if not currency:
        logger.error(f"Bitcoin currency does not exists")
        return

    currency_data = client.get_blockchain_stats(symbol="BTC")
    if currency_data:
        schema = CreateBlockSchema(
            currency_id=currency.id,
            provider_id=coin_market_cap_provider.id,
            number=currency_data["data"]["BTC"]["total_blocks"],
        )

        Block.objects.get_or_create(
            number=schema.number,
            currency_id=schema.currency_id,
            defaults={
                "provider_id": schema.provider_id,
                "best_block_time": schema.best_block_time,
            },
        )
    else:
        logger.error(f"Bitcoin data is empty")
        return


def refresh_eth_latest_blocks_data():
    block_chair_provider = Provider.objects.filter(name="BlockChair").first()
    if not block_chair_provider:
        logger.error("BlockChair provider does not exists")
        return

    client = BlockChairClient()

    currency = Currency.objects.filter(name__iexact="Ethereum").first()
    if not currency:
        logger.error(f"Ethereum currency does not exists")
        return

    currency_data = client.get_blockchain_stats(chain="ethereum")

    if currency_data:
        best_block_time = datetime.strptime(
            currency_data["data"]["best_block_time"], "%Y-%m-%d %H:%M:%S"
        )
        schema = CreateBlockSchema(
            currency_id=currency.id,
            provider_id=block_chair_provider.id,
            number=currency_data["data"]["blocks"],
            best_block_time=best_block_time,
        )

        Block.objects.get_or_create(
            number=schema.number,
            currency_id=schema.currency_id,
            defaults={
                "provider_id": schema.provider_id,
                "best_block_time": schema.best_block_time,
            },
        )
    else:
        logger.error(f"Ethereum data is empty")
        return
