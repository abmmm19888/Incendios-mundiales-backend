#!/usr/bin/env python3

from core.database import engine
from sqlalchemy import Uuid, Column, Integer, String, Text, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship, declarative_base
from uuid import uuid4

Base = declarative_base()

class User(Base):
	__tablename__ = 'user'

	uuid = Column(Uuid, primary_key = True, default = uuid4)
	username = Column(Text(), unique = True, nullable = False)
	hashed_password = Column(Text(), nullable = False)
	name = Column(Text())
	email = Column(String(360))

	articles = relationship('Article', back_populates = 'user')

class Article(Base):
	__tablename__ = 'article'

	uuid = Column(Uuid, primary_key = True, default = uuid4)
	title = Column(Text(), nullable = False)
	content = Column(Text(), nullable = False)
	creation_date = Column(DateTime(), nullable = False)
	modification_date = Column(DateTime(), nullable = False)
	image = Column(Text())
	user_uuid = Column(Uuid, ForeignKey('user.uuid'), nullable = False)
	
	user = relationship('User', back_populates = 'articles')
	taggings = relationship('Tagging', back_populates = 'article')

class Tagging(Base):
	__tablename__ = 'tagging'
	
	uuid = Column(Uuid, primary_key = True, default = uuid4)
	article_uuid = Column(Uuid, ForeignKey('article.uuid'), nullable = True)
	tag_uuid = Column(Uuid, ForeignKey('tag.uuid'), nullable = True)
	
	article = relationship('Article', back_populates = 'taggings')
	tag = relationship('Tag', back_populates = 'taggings')

class Tag(Base):
	__tablename__ = 'tag'
	
	uuid = Column(Uuid, primary_key = True, default = uuid4)
	tag = Column(Text(), nullable = False)
	
	taggings = relationship('Tagging', back_populates = 'tag')

Base.metadata.create_all(engine)
