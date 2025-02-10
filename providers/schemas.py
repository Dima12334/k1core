from uuid import UUID
from pydantic import BaseModel, Field
from providers.constants import ProviderConstants


class ReadProviderSchema(BaseModel):
    id: UUID
    name: str


class CreateProviderSchema(BaseModel):
    name: str = Field(max_length=ProviderConstants.NAME_MAX_LENGTH)
