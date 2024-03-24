from pydantic import BaseModel, Extra, Field, PositiveInt
from typing import Optional

from app.schemas.base import AbstractBaseSchema


class CharityProjectCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    description: str = Field(..., min_length=1)
    full_amount: PositiveInt


class CharityProjectUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = Field(None, min_length=1)
    full_amount: Optional[PositiveInt]

    class Config:
        extra = Extra.forbid


class CharityProjectDB(AbstractBaseSchema, CharityProjectCreate):
    id: int

    class Config:
        orm_mode = True
