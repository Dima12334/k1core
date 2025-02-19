from django.db import models

from common.models import BaseModelMixin
from providers.constants import ProviderConstants


class Provider(BaseModelMixin):
    name = models.CharField(max_length=ProviderConstants.NAME_MAX_LENGTH, unique=True)

    class Meta:
        verbose_name = "Provider"
        verbose_name_plural = "Providers"
        db_table = "providers"

    def __str__(self):
        return self.name
