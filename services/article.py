#!/user/bin/env python3

from sqlalchemy.orm import Session
from core.models import Article, User
from core.types import Undefined
from schemas.article import ArticleCreationData, ArticleUpdateData
from datetime import datetime

class ArticleService:
	@staticmethod
	def create_article(data: ArticleCreationData, user: User, session: Session):
		date = datetime.utcnow()
		image = None # TODO
		article = Article(
			title = data.title,
			content = data.content,
			creation_date = date,
			modification_date = date,
			image = image,
			user_uuid = user.uuid)
		session.add(article)
		session.commit()
		session.refresh(article)
		return article
	
	@staticmethod
	def read_article(uuid, session: Session):
		article = session.query(Article).get(uuid)
		return article
	
	@staticmethod
	def update_article(data: ArticleUpdateData, uuid, user: User, session: Session):
		article = session.query(Article).get(uuid)
		article.modification_date = datetime.utcnow()
		
		if data.title is not Undefined:
			article.title = data.title
		if data.content is not Undefined:
			article.content = data.content
		
		session.commit()
		session.refresh(article)
		return article
	
	@staticmethod
	def delete_article(uuid, user: User, session: Session):
		article = session.query(Article).get(uuid)
		session.delete(article)
		session.commit()
		
	@staticmethod
	def list_articles(session: Session):
		articles = session.query(Article).all()
		return articles

