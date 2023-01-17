from uuid import UUID

from core.deps import db_context
from .models import Website, Article
from .schemas import WebsiteSchemaIn, WebsiteSchemaOut, ArticleSchemaOut


def crud_add_website(website: WebsiteSchemaIn):
    db_website = Website(**website.dict())
    with db_context() as db:
        db.add(db_website)
        db.commit()
        db.refresh(db_website)
    return db_website


def crud_get_websites():
    with db_context() as db:
        websites = db.query(Website).all()
    if not websites:
        return None
    return [WebsiteSchemaOut(**item.__dict__) for item in websites]


def crud_get_website(website_id: UUID):
    with db_context() as db:
        website = db.query(Website).filter(Website.id == website_id).first()
    if not website:
        return None
    return WebsiteSchemaOut(**website.__dict__)


def crud_get_articles():
    with db_context() as db:
        articles = db.query(Article).all()
    if not articles:
        return None
    return [ArticleSchemaOut(**item.__dict__) for item in articles]


def crud_create_article_and_entities(website_id: UUID, href: str, entities: list):
    return None
