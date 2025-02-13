from uuid import UUID
from pydantic import BaseModel, Field
from providers.constants import ProviderConstants


class ReadProviderSchema(BaseModel):
    id: UUID
    name: str

    class Config:
        orm_mode = True
