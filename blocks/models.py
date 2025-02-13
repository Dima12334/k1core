from django.db import models

from common.models import BaseModelMixin, Currency
from providers.models import Provider


class Block(BaseModelMixin):
    currency = models.ForeignKey(
        Currency, on_delete=models.PROTECT, related_name="blocks"
    )
    provider = models.ForeignKey(
        Provider, on_delete=models.PROTECT, related_name="blocks"
    )
    number = models.PositiveIntegerField()
    best_block_time = models.DateTimeField(null=True, default=None)

    class Meta:
        verbose_name = "Block"
        verbose_name_plural = "Blocks"
        db_table = "blocks"
        unique_together = ("currency", "number")

    def __str__(self):
        return f"{self.currency.name}: {self.number}"
