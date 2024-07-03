#!/usr/bin/env python3

from pydantic import BaseModel
from datetime import datetime
from core.types import Undefined

class ArticleCreationData(BaseModel):
	title: str = ''
	content: str  = ''

class ArticleUpdateData(BaseModel):
	title: str = Undefined
	content: str = Undefined
