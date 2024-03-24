from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, PositiveInt

from app.constants import TIME_EXAMPLE


class AbstractBaseSchema(BaseModel):
    full_amount: PositiveInt
    invested_amount: int
    fully_invested: bool
    create_date: datetime = Field(..., example=TIME_EXAMPLE)
    close_date: Optional[datetime] = Field(None, example=TIME_EXAMPLE)
