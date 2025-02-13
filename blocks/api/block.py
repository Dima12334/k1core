from typing import List, Optional
from uuid import UUID

from asgiref.sync import sync_to_async
from django.core.paginator import Paginator

from blocks.models import Block
from fastapi import HTTPException


class BlockAPI:
    @classmethod
    async def get(
        cls,
        currency_name: Optional[str],
        provider_name: Optional[str],
        page: int,
        limit: int
    ) -> List[Block]:
        blocks = Block.objects.select_related("currency", "provider").order_by("currency__name")

        # Apply filters
        if currency_name:
            blocks = blocks.filter(currency__name__iexact=currency_name)
        if provider_name:
            blocks = blocks.filter(provider__name__iexact=provider_name)

        # Pagination
        paginator = Paginator(blocks, limit)
        page_obj = await sync_to_async(paginator.get_page)(page)
        blocks = await sync_to_async(list)(page_obj.object_list)
        return blocks

    @classmethod
    async def retrieve_by_id(cls, block_id: UUID) -> Block:
        try:
            block = await sync_to_async(Block.objects.select_related("currency", "provider").get)(
                id=block_id,
            )
            return block
        except Block.DoesNotExist:
            raise HTTPException(status_code=404, detail="Block not found")

    @classmethod
    async def retrieve_by_currency_id_and_number(
        cls,
        currency_id: UUID,
        number: int,
    ) -> Block:
        try:
            block = await sync_to_async(Block.objects.select_related("currency", "provider").get)(
                currency_id=currency_id,
                number=number
            )
            return block
        except Block.DoesNotExist:
            raise HTTPException(status_code=404, detail="Block not found")

