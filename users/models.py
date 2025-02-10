from django.contrib.auth.models import AbstractUser
from common.models import BaseModelMixin


class User(AbstractUser, BaseModelMixin):

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        db_table = "users"
        ordering = ["-created_at"]
