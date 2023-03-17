from datetime import datetime

from pydantic import BaseModel


class PostBase(BaseModel):
    title: str
    text: str

    class Config:
        orm_mode = True


class PostList(PostBase):
    id: int
    user: int


class PostCreate(PostBase):
    date: datetime
    user_id: int
