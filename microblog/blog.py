from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.utils import get_db
from . import service, schemas

router = APIRouter()


@router.get("/", response_model=List[schemas.PostList])
def post_list(db: Session = Depends(get_db)):
    return service.get_post_list(db)


@router.post("/")
def post_create(item: schemas.PostCreate, db: Session = Depends(get_db)):
    return service.create_post(db, item)
