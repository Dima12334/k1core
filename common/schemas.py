from uuid import UUID
from pydantic import BaseModel, Field
from common.constants import CurrencyConstants


class ReadCurrencySchema(BaseModel):
    id: UUID
    name: str


class CreateCurrencySchema(BaseModel):
    name: str = Field(max_length=CurrencyConstants.NAME_MAX_LENGTH)
