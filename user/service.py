from datetime import datetime

from fastapi import HTTPException
from sqlalchemy.orm import Session

from .models import User
from .schemas import UserCreate


def user_register(db: Session, item: UserCreate):
    item = item.dict()
    item["date"] = datetime.now()
    item["id"] = len(get_user_list(db)) + 1
    if get_user_by_username(db, item["username"]) is not None:
        raise HTTPException(status_code=400, detail=f"username '{item['username']}' is exist")
    if get_user_by_email(db, item["email"]) is not None:
        raise HTTPException(status_code=400, detail=f"email '{item['email']}' is exist")
    user = User(**item)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user_by_username(db: Session, username: str):
    return db.query(User).filter_by(username=username).first()


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter_by(email=email).first()


def get_user_by_id(db: Session, user_id: str | int):
    return db.query(User).get(user_id)


def check_user_in_db(db: Session, user: User):
    return db.query(User).get(user)


def get_user_list(db: Session):
    return db.query(User).all()
