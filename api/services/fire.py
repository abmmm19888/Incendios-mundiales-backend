#!/usr/bin/env python3

from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from core.models import Fire, User
from core.types import Undefined
from schemas.fire import FireCreationData, FireUpdateData
from datetime import datetime

class FireService:
	@staticmethod
	def create_fire(data: FireCreationData, user: User, session: Session):
		# TODO Check user permissions.
		fire = Fire(
			latitude = data.latitude,
			longitude = data.longitude,
			date = data.date,
			confidence = data.confidence)
		
		session.add(fire)

		try:
			session.commit()
		except IntegrityError:
			return None

		session.refresh(fire)
		return fire
	
	@staticmethod
	def read_fire(uuid, session: Session):
		fire = session.query(Fire).get(uuid)
		return fire
	
	@staticmethod
	def update_fire(data: FireUpdateData, uuid, user: User, session: Session):
		# TODO Check user permissions.
		fire = session.query(Fire).get(uuid)

		if data.latitude is not Undefined:
			fire.latitude = data.latitude
		if data.longitude is not Undefined:
			fire.longitude = data.longitude
		if data.date is not Undefined:
			fire.date = data.date
		if data.confidence is not Undefined:
			fire.confidence = data.confidence
		
		session.commit()
		session.refresh(fire)
		return fire
	
	@staticmethod
	def delete_fire(uuid, user: User, session: Session):
		# TODO Check user permissions.
		fire = session.query(Fire).get(uuid)
		session.delete(fire)
		session.commit()
		
	@staticmethod
	def list_fires(session: Session):
		fires = session.query(Fire).all()
		return fires
