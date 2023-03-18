from typing import Union

from sqlalchemy.orm import Session
from fastapi import APIRouter, Body, Depends, HTTPException

from core.utils import get_db
from . import schemas, models, service
from auth.auth_handler import signJWT

app = APIRouter()


@app.post("/user/signup", tags=["user"])
def create_user(user: schemas.UserCreate = Body(...), db: Session = Depends(get_db)):
    service.user_register(db, user)
    return signJWT(user.email)


def check_user(data: schemas.UserLogin, db: Session = Depends(get_db)):
    users = service.get_user_list(db)
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
    return False


@app.post("/user/login", tags=["user"])
def user_login(user: schemas.UserLogin = Body(...), db: Session = Depends(get_db)):
    if check_user(user, db):
        return signJWT(user.email)
    return {
        "error": "wrong login details!"
    }
