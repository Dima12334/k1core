from typing import List, Optional
from uuid import UUID

from fastapi import APIRouter, Depends, Request, Query

from blocks.api.block import BlockAPI
from blocks.models import Block
from blocks.schemas import ReadBlockSchema
from users.dependencies.auth import get_current_user
from users.models import User


block_router = APIRouter()


@block_router.get("/", response_model=List[ReadBlockSchema])
async def get(
    request: Request,
    current_user: User = Depends(get_current_user),
    currency_name: Optional[str] = Query(None, description="Filter by currency name"),
    provider_name: Optional[str] = Query(None, description="Filter by provider name"),
    page: int = Query(1, ge=1, description="Page number"),
    limit: int = Query(20, ge=1, le=100, description="Number of items per page"),
) -> List[Block]:
    return await BlockAPI.get(
        currency_name=currency_name, provider_name=provider_name, page=page, limit=limit
    )


@block_router.get("/{block_id}", response_model=ReadBlockSchema)
async def retrieve_by_id(
    request: Request, block_id: UUID, current_user: User = Depends(get_current_user)
) -> Block:
    return await BlockAPI.retrieve_by_id(block_id=block_id)


@block_router.get("/{currency_id}/{number}", response_model=ReadBlockSchema)
async def retrieve_by_currency_id_and_number(
    request: Request,
    currency_id: UUID,
    number: int,
    current_user: User = Depends(get_current_user),
) -> Block:
    return await BlockAPI.retrieve_by_currency_id_and_number(
        currency_id=currency_id, number=number
    )
