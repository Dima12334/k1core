from uuid import UUID
from pydantic import BaseModel, Field
from common.constants import CurrencyConstants


class ReadCurrencySchema(BaseModel):
    id: UUID
    name: str

    class Config:
        orm_mode = True
