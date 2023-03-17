from sqlalchemy.orm import Session

from .models import Post
from .schemas import PostCreate


def get_post_list(db: Session):
    return db.query(Post).all()


def create_post(db: Session, item: PostCreate, user_id):
    item = item.dict()
    item["id"] = len(get_post_list(db)) + 1
    item["user"] = user_id
    post = Post(**item)
    db.add(post)
    db.commit()
    db.refresh(post)
    return post
