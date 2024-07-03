#!/usr/bin/env python3

from pydantic import BaseModel

class UserCreationData(BaseModel):
	username: str
	password: str
	name: str | None = None
	email: str | None = None
