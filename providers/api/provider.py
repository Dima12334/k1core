from typing import List, Optional
from uuid import UUID

from asgiref.sync import sync_to_async
from django.core.paginator import Paginator

from blocks.models import Block
from fastapi import Request, HTTPException

from providers.models import Provider
from users.models import User


class ProviderAPI:
    @classmethod
    async def get(cls) -> List[Provider]:
        providers = await sync_to_async(Provider.objects.all)()
        providers = await sync_to_async(list)(providers)
        return providers
