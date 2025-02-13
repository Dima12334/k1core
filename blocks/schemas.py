from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel
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
        orm_mode = True
