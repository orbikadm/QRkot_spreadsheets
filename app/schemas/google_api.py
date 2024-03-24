from pydantic import BaseModel, Field, AnyHttpUrl


class GoogleAPIResponseSchema(BaseModel):
    url: AnyHttpUrl = Field(
        ...,
        example='https://docs.google.com/spreadsheets/d/spreadsheetid'
    )
