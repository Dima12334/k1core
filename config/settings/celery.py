from celery.schedules import crontab
from config.settings.dev import *


CELERY_BROKER_URL = env.str("CELERY_BROKER_URL", "redis://127.0.0.1:6379/0")
CELERY_RESULT_BACKEND = env.str("CELERY_RESULT_BACKEND", "redis://127.0.0.1:6379/0")

CELERYBEAT_SCHEDULE = {
    "get_latest_blocks_data": {
        "task": "common.tasks.get_latest_blocks_data",
        "schedule": crontab(minute="*/1"),
    }
}
