#!/user/bin/env python3

import core.models

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import token, user, article

app = FastAPI()

# https://fastapi.tiangolo.com/tutorial/cors/
app.add_middleware(
    CORSMiddleware,
    allow_origins = ['http://localhost:5173'],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

app.include_router(token.router)
app.include_router(user.router)
app.include_router(article.router)
