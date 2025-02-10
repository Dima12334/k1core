import os
from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.celery")

app = Celery("k1core")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
