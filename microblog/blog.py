from typing import List

from fastapi import APIRouter, Depends, Request, Body
from sqlalchemy.orm import Session

from core.utils import get_db
from . import service, schemas
from auth.auth_bearer import JWTBearer

router = APIRouter()


@router.get("/", response_model=List[schemas.PostList], tags=["posts"])
def post_list(db: Session = Depends(get_db)):
    return service.get_post_list(db)


@router.post("/", dependencies=[Depends(JWTBearer())], tags=["posts"])
async def post_create(item: schemas.PostCreate, db: Session = Depends(get_db)):
    return service.create_post(db, item)


@router.get("/post", response_model=schemas.SinglePost, tags=['posts'])
def get_single_post(post_id: int, db: Session = Depends(get_db)):
    return service.get_single_post(db, post_id)
