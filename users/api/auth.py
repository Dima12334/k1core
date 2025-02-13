from logging import getLogger

from fastapi import Request
from fastapi.security import OAuth2PasswordRequestForm

from common.exceptions import (
    InvalidCredentialsException,
    InvalidUsernameOrPasswordException,
)
from users.jwt import create_access_token_response
from users.models import User
from users.password import verify_password
from users.schemas import Token

logger = getLogger(__name__)


class AuthAPI:
    @classmethod
    async def login(
        cls, request: Request, form_data: OAuth2PasswordRequestForm
    ) -> Token:
        credentials = {"username": form_data.username, "password": form_data.password}

        if all(credentials.values()):
            user = await cls()._authenticate_user(**credentials)
        else:
            raise InvalidCredentialsException()
        return create_access_token_response({"sub": str(user.id)})

    async def _authenticate_user(self, username: str, password: str) -> User:
        user = await User.objects.filter(username=username).afirst()
        if not user:
            raise InvalidUsernameOrPasswordException()
        if not verify_password(password, user.password) or not user.is_active:
            raise InvalidUsernameOrPasswordException()
        return user
