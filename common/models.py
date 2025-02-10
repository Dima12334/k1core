from django.db import models
import uuid


class BaseModelMixin(models.Model):
    class Meta:
        abstract = True

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(db_index=True, auto_now_add=True)
    updated_at = models.DateTimeField(db_index=True, auto_now=True)


class Currency(BaseModelMixin):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = "Currency"
        verbose_name_plural = "Currencies"
        db_table = "currencies"

    def __str__(self):
        return self.name
