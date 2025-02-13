from asgiref.sync import sync_to_async
from fastapi import HTTPException, Request

from users.models import User
from users.password import hash_password
from users.schemas import CreateUserSchema


class UserAPI:
    @classmethod
    def get(cls, current_user: User) -> User:
        return current_user

    @classmethod
    async def create(cls, schema: CreateUserSchema) -> User:
        user = await User.objects.filter(username=schema.username).afirst()
        if user:
            raise HTTPException(status_code=400, detail="Username already registered")
        schema.password = hash_password(schema.password)
        return await sync_to_async(User.objects.create)(**schema.dict())
