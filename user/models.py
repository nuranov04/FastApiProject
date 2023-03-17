from sqlalchemy import Column, String, Integer, DateTime

from core.db import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, unique=True, index=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    date = Column(DateTime)
    password = Column(String(length=25))
