from fastapi import APIRouter, Depends, Request

from users.api import UserAPI
from users.dependencies.auth import get_current_user
from users.models import User
from users.schemas import ReadUserSchema, CreateUserSchema

user_router = APIRouter()


@user_router.get("/", response_model=ReadUserSchema)
async def get(request: Request, current_user: User = Depends(get_current_user)) -> User:
    return UserAPI.get(current_user=current_user)


@user_router.post("/", response_model=ReadUserSchema)
async def create(request: Request, schema: CreateUserSchema) -> User:
    return await UserAPI.create(schema=schema)
