#!/usr/bin/env python3

from os import getenv

FRONTEND_HOST = getenv('FRONTEND_HOST')
FRONTEND_PORT = getenv('FRONTEND_PORT')

if FRONTEND_HOST == None or FRONTEND_PORT == None:
    raise Exception("Frontend configuration not found")

import core.models

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import token, user, fire

app = FastAPI()

# https://fastapi.tiangolo.com/tutorial/cors/
app.add_middleware(
    CORSMiddleware,
    allow_origins = [f'http://{FRONTEND_HOST}:{FRONTEND_PORT}'],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

app.include_router(token.router)
app.include_router(user.router)
app.include_router(fire.router)
