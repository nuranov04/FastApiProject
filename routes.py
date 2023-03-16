from fastapi import APIRouter

from microblog import blog

router = APIRouter()

router.include_router(blog.router, prefix="/blog")
