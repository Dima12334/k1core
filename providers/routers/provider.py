from typing import List
from fastapi import APIRouter, Depends, Request

from providers.api.provider import ProviderAPI
from providers.models import Provider
from providers.schemas import ReadProviderSchema
from users.dependencies.auth import get_current_user
from users.models import User


provider_router = APIRouter()


@provider_router.get("/", response_model=List[ReadProviderSchema])
async def get(request: Request, current_user: User = Depends(get_current_user)) -> List[Provider]:
    return await ProviderAPI.get()
