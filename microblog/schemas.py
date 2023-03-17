from datetime import datetime

from pydantic import BaseModel

from user.models import User


class PostBase(BaseModel):
    title: str
    text: str


class PostList(PostBase):
    id: int
    data: datetime

    class Config:
        orm_mode = True


class PostCreate(PostBase):
    title: str
    text: str
    date: datetime
    # user: User
