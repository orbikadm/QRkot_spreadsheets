from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, PositiveInt

from app.schemas.base import AbstractBaseSchema
from app.constants import TIME_EXAMPLE


class DonationCreate(BaseModel):
    full_amount: PositiveInt
    comment: Optional[str]


class DonationDB(DonationCreate):
    id: int
    create_date: datetime = Field(None, example=TIME_EXAMPLE)

    class Config:
        orm_mode = True


class DonationAdminDB(AbstractBaseSchema, DonationDB):
    user_id: int

    class Config:
        orm_mode = True
