from fastapi import APIRouter, Depends, Request
from fastapi.security import OAuth2PasswordRequestForm

from users.api import AuthAPI
from users.schemas import Token

auth_router = APIRouter()


@auth_router.post("/login", response_model=Token)
async def login(
    request: Request, form_data: OAuth2PasswordRequestForm = Depends()
) -> Token:
    return await AuthAPI.login(request, form_data)
