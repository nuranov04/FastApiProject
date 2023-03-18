import uvicorn
from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import Response, JSONResponse

from core.db import SessionLocal
from routes import router

app = FastAPI(
    title="Blog Api"
)


def on_auth_error(request: Request, exc: Exception):
    return JSONResponse({"error": str(exc)}, status_code=401)


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
