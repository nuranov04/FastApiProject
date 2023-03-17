from datetime import datetime

from sqlalchemy.orm import Session

from .models import User
from .schemas import UserCreate


def user_register(db: Session, item: UserCreate):
    item.date = datetime.now()
    item.id = len(get_user_list(db)) + 1

    user = User(**item)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user_list(db: Session):
    return db.query(User).all()
