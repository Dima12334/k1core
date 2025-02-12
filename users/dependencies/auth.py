from jose import JWTError

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from common.exceptions import InvalidTokenException
from users.jwt import jwt_decode_handler
from users.models import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


async def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    try:
        payload = jwt_decode_handler(token)
    except JWTError:
        raise InvalidTokenException()

    user = await User.objects.filter(id=payload.get("sub", "")).afirst()
    if not user:
        raise InvalidTokenException()
    return user
