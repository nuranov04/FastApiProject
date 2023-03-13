from datetime import date
from typing import List

from pydantic import BaseModel, Field


class Genre(BaseModel):
    name: str


class Book(BaseModel):
    title: str
    writer: str
    duration: str
    date: date
    summary: str
    genres: List[Genre] = []
    pages: int = 10


class Author(BaseModel):
    first_name: str = Field(..., max_length=25)
    last_name: str
    age: int = Field(
        20, gt=15, lt=120, description="Author must be more than 15 and less than 120"
    )

    # @validator("age")
    # def check_age(cls, v):
    #     if v < 15 > 90:
    #         raise ValueError("Автор должен быть старше 15 лет)")
    #     return v
