from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.utils import get_db
from . import service
router = APIRouter()


@router.get("/")
def post_list(db: Session = Depends(get_db)):
    posts = service.get_post_list(db)
    return posts
