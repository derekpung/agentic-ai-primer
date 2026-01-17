from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware
from auth.router import router as auth_router
from llm.router import router as llm_router

import os

app = FastAPI()
app.add_middleware(
    SessionMiddleware,
    secret_key=os.getenv("SESSION_SECRET", ""),
)

app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(llm_router, prefix="/llm", tags=["llm"])
