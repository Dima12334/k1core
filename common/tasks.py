import logging
from datetime import datetime

from celery import shared_task

from blocks.models import Block
from common.clients.http_block_chair_client import BlockChairClient
from common.models import Currency
from providers.models import Provider


logger = logging.getLogger(__name__)


def _get_latest_blocks_data(provider: Provider, currency_name: str):
    client = BlockChairClient()

    currency = Currency.objects.filter(name__iexact=currency_name).first()
    if not currency:
        logger.error(f"{currency_name} currency does not exists")
        return

    currency_data = client.get_blockchain_stats(chain=currency_name.lower())

    if currency_data:
        best_block_time = datetime.strptime(
            currency_data['data']['best_block_time'], "%Y-%m-%d %H:%M:%S"
        )
        Block.objects.get_or_create(
            number=currency_data['data']['blocks'],
            currency=currency,
            defaults={
                'provider': provider,
                'best_block_time': best_block_time,
            }
        )
    else:
        logger.error(f"{currency_name} data is empty")
        return


@shared_task()
def get_latest_blocks_data():
    provider = Provider.objects.filter(name='BlockChair').first()
    if not provider:
        logger.error("BlockChair provider does not exists")
        return

    _get_latest_blocks_data(provider=provider, currency_name='Bitcoin')
    _get_latest_blocks_data(provider=provider, currency_name='Ethereum')
