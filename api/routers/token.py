#!/usr/bin/env python3

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from core.database import get_session
from core.auth import get_user
from services.token import TokenService
from services.user import UserService

router = APIRouter()

@router.post("/token")
async def create_token(data: OAuth2PasswordRequestForm = Depends(OAuth2PasswordRequestForm), session: Session = Depends(get_session)):
	user = UserService.read_user_by_credentials(data.username, data.password, session)
	
	if not user:
		raise HTTPException(
			status_code = status.HTTP_401_UNAUTHORIZED,
			detail = "Incorrect username or password",
			headers = {"WWW-Authenticate": "Bearer"})

	token = TokenService.create_token(user.username)
	return token
