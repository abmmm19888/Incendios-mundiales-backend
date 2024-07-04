#!/usr/bin/env python3

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.database import get_session
from core.auth import get_user
from schemas.user import UserCreationData
from services.user import UserService

router = APIRouter()

@router.post("/user", tags = ['user'])
async def create_user(data: UserCreationData, session: Session = Depends(get_session)):
	user = UserService.create_user(data, session)
	return {'unavailableUsername': user is None, 'user': user}

@router.get("/authenticated-user", tags = ['user'])
async def read_authenticated_user(user = Depends(get_user), session: Session = Depends(get_session)):
	return {'user': user}
