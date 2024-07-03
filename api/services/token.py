#!/usr/bin/env python3

from sqlalchemy.orm import Session
from datetime import datetime, timedelta, timezone
from core.configuration import JWT_SECRET_KEY, JWT_EXPIRE_TIME, JWT_ALGORITHM
from jose import jwt
from schemas.token import Token

class TokenService:
	@staticmethod
	def create_token(username: str):
		expire_delta = timedelta(minutes = JWT_EXPIRE_TIME)
		expire = datetime.now(timezone.utc) + expire_delta
		data = {"sub": username, "exp": expire}
		access_token = jwt.encode(data, JWT_SECRET_KEY, algorithm = JWT_ALGORITHM)
		return Token(access_token = access_token, token_type = "bearer")

	@staticmethod
	def read_token_username(token: str):
		data = jwt.decode(token, JWT_SECRET_KEY, algorithms = [JWT_ALGORITHM])
		username: str = data.get("sub")
		return username
