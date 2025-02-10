from django.db import models

from common.models import BaseModelMixin, Currency
from providers.models import Provider


class Block(BaseModelMixin):
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT, related_name="blocks")
    provider = models.ForeignKey(Provider, on_delete=models.PROTECT, related_name="blocks")
    number = models.PositiveIntegerField()
    blockchain_created_at = models.DateTimeField(null=True, default=None)

    class Meta:
        verbose_name = "Block"
        verbose_name_plural = "Blocks"
        db_table = "blocks"

    def __str__(self):
        return f"{self.currency.name}: {self.number}"
