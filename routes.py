from fastapi import APIRouter

from microblog import blog
from user import users

router = APIRouter()

router.include_router(blog.router, prefix="/posts")
router.include_router(users.app, prefix="/users")
