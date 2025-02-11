from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel, Field
from common.schemas import ReadCurrencySchema
from providers.schemas import ReadProviderSchema


class ReadBlockSchema(BaseModel):
    id: UUID
    currency: ReadCurrencySchema
    provider: ReadProviderSchema
    number: int
    best_block_time: Optional[datetime]

    class Config:
        arbitrary_types_allowed = True


class CreateBlockSchema(BaseModel):
    currency_id: UUID
    provider_id: UUID
    number: int = Field(gt=0)
    best_block_time: Optional[datetime]
