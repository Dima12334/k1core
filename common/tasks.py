from celery import shared_task
from common.utils import refresh_btc_latest_blocks_data, refresh_eth_latest_blocks_data


@shared_task()
def get_latest_blocks_data():
    refresh_btc_latest_blocks_data()
    refresh_eth_latest_blocks_data()
