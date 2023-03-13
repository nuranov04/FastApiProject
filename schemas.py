from datetime import date
from typing import List

from pydantic import BaseModel, validator


class Genre(BaseModel):
    name: str


class Book(BaseModel):
    title: str
    writer: str
    duration: str
    date: date
    summary: str
    genres: List[Genre]
    pages: int


class Author(BaseModel):
    first_name: str
    last_name: str
    age: int

    @validator("age")
    def check_age(cls, v):
        if v < 15:
            raise ValueError("Bla bla bla")

