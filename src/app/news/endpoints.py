from fastapi import APIRouter, Depends, HTTPException, Path

from app.core.celery_app import celery_app
from .schemas import WebsiteSchemaIn, WebsiteSchemaOut, ArticleSchemaOut
from .crud import crud_add_website, crud_get_websites, crud_get_articles


router = APIRouter()


@router.post('/news/websites', response_model=WebsiteSchemaIn)
def add_website(
    item_in: ItemSchema,
):
    website_obj = crud_add_website(item_in)
    celery_app.send_task("process_news_website", args=[website_obj.id])
    return website_obj


@router.post('/news/websites', response_model=list[WebsiteSchemaOut])
def get_websites():
    return crud_get_websites()


@router.post('/news/articles', response_model=list[ArticleSchemaOut])
def get_articles():
    return crud_get_articles()
