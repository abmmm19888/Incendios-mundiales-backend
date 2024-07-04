#!/usr/bin/env python3

from core.database import engine
from sqlalchemy import Uuid, Column, Text, Integer, Float, Date, UniqueConstraint
from sqlalchemy.orm import declarative_base
from uuid import uuid4

Base = declarative_base()

class User(Base):
	__tablename__ = 'user'

	uuid = Column(Uuid, primary_key = True, default = uuid4)
	username = Column(Text, unique = True, nullable = False)
	hashed_password = Column(Text, nullable = False)

class Fire(Base):
	__tablename__ = 'fire'
	
	uuid = Column(Uuid, primary_key = True, default = uuid4)
	latitude = Column(Float, nullable = False)
	longitude = Column(Float, nullable = False)
	date = Column(Date, nullable = False)
	confidence = Column(Integer)

	__table_args__ = (UniqueConstraint('latitude', 'longitude', 'date'), )

Base.metadata.create_all(engine)
