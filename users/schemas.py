from uuid import UUID
from pydantic import BaseModel, Field
from users.constants import UserConstants


class ReadUserSchema(BaseModel):
    id: UUID
    username: str


class CreateUserSchema(BaseModel):
    username: str = Field(max_length=UserConstants.USERNAME_MAX_LENGTH)
    password: str = Field(max_length=UserConstants.PASSWORD_MAX_LENGTH)
