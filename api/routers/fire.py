#!/usr/bin/env python3

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.database import get_session
from core.auth import get_user

from schemas.fire import FireCreationData, FireUpdateData
from services.fire import FireService

router = APIRouter()

@router.post("/fire", tags = ['fire'])
async def create_fire(data: FireCreationData, user = Depends(get_user), session: Session = Depends(get_session)):
	fire = FireService.create_fire(data, user, session)
	return fire if fire else {}

@router.get("/fire/{uuid}", tags = ['fire'])
async def read_fire(uuid, session: Session = Depends(get_session)):
	fire = FireService.read_fire(uuid, session)
	return fire

@router.patch("/fire/{uuid}", tags = ['fire'])
async def update_fire(data: FireUpdateData, uuid, user = Depends(get_user), session: Session = Depends(get_session)):
	fire = FireService.update_fire(data, uuid, user, session)
	return fire

@router.delete("/fire/{uuid}", tags = ['fire'])
async def delete_fire(uuid, user = Depends(get_user), session: Session = Depends(get_session)):
	FireService.delete_fire(uuid, user, session)
	return {}

@router.get("/fire", tags = ['fire'])
async def list_fires(session: Session = Depends(get_session)):
	fires = FireService.list_fires(session)
	return fires
