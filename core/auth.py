#!/user/bin/env python3

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from core.database import get_session
from services.user import UserService

oauth2_scheme = OAuth2PasswordBearer(tokenUrl = "token")

async def get_user(token: str = Depends(oauth2_scheme), session: Session = Depends(get_session)):
	user = UserService.read_user_by_token(token, session)

	if user is None:
		raise HTTPException(
		status_code=status.HTTP_401_UNAUTHORIZED,
		detail="Could not validate credentials",
		headers={"WWW-Authenticate": "Bearer"},
	)

	return user