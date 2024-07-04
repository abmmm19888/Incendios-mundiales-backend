#!/usr/bin/env python3

from pydantic import BaseModel
from datetime import datetime # FIXME Should be date.
from core.types import Undefined

class FireCreationData(BaseModel):
	latitude: float = Undefined
	longitude: float = Undefined
	date: datetime = Undefined
	confidence: int = Undefined

class FireUpdateData(BaseModel):
	latitude: float = Undefined
	longitude: float = Undefined
	date: datetime = Undefined
	confidence: int = Undefined
