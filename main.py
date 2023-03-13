from typing import List

from fastapi import FastAPI, Query, Path, Body

from schemas import Book, Author

app = FastAPI()


@app.post('/book/create/')
def create_book(item: Book, author: Author, quantity: int = Body(...)):
    return {"book": item, "author": author}


@app.post('/author/create/')
def create_author(author: Author = Body(..., embed=True)):
    return {"author": author}


@app.get("/book")
def get_book(q: List[str] = Query(["test", "test2"], description="Search Book", deprecated=True)):
    return q


@app.get("/book/{pk}")
def get_single_book(pk: int = Path(..., gt=1, le=20), pages: int = Query(None, gt=10, lt=500)):
    return {"pk": pk, "pages": pages}


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/")
def home():
    return {"key": "value"}


@app.get("/item/{pk}")
def get_item(pk: int, q: int = None):
    return {"key": pk, "q": q}


@app.get("/user/{pk}/items/{item}/")
def get_user_item(pk: int, item: str):
    return {"user": pk, "item": item}
