#!/user/bin/env python3

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.database import get_session
from core.auth import get_user

from schemas.article import ArticleCreationData, ArticleUpdateData
from services.article import ArticleService

router = APIRouter()

@router.post("/article")
async def create_article(data: ArticleCreationData, user = Depends(get_user), session: Session = Depends(get_session)):
	article = ArticleService.create_article(data, user, session)
	return article

@router.get("/article/{uuid}")
async def read_article(uuid, session: Session = Depends(get_session)):
	article = ArticleService.read_article(uuid, session)
	return article

@router.patch("/article/{uuid}")
async def update_article(data: ArticleUpdateData, uuid, user = Depends(get_user), session: Session = Depends(get_session)):
	article = ArticleService.update_article(data, uuid, user, session)
	return article

@router.delete("/article/{uuid}")
async def delete_article(uuid, user = Depends(get_user), session: Session = Depends(get_session)):
	ArticleService.delete_article(uuid, user, session)
	return {}

@router.get("/article")
async def list_articles(session: Session = Depends(get_session)):
	articles = ArticleService.list_articles(session)
	return articles
