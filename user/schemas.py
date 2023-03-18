from datetime import datetime

from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

    class Config:
        schema_extra = {
            "example": {
                "username": "abdulazeez",
                "email": "abdulazeez@x.com",
                "password": "weakpassword"
            }
        }


class UserInfo(UserCreate):
    id: int
    date: datetime


class UserLogin(BaseModel):
    email: EmailStr
    password: str

    class Config:
        schema_extra = {
            "example": {
                "email": "abdulazeez@x.com",
                "password": "weakpassword"
            }
        }
