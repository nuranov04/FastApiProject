from sqlalchemy.orm import Session
from fastapi import HTTPException

from .models import Post
from .schemas import PostCreate,SinglePost


def get_post_list(db: Session):
    return db.query(Post).all()


def create_post(db: Session, item: PostCreate):
    item = item.dict()
    print(item)
    item["id"] = len(get_post_list(db)) + 1
    print(item)
    post = Post(**item)
    db.add(post)
    db.commit()
    db.refresh(post)
    return post


def get_single_post(db: Session, post_id: int):
    post = db.query(Post).get(post_id)
    if post is None:
        raise HTTPException(status_code=405, detail="item not found")
    return post
