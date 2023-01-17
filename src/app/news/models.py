import uuid

from app.core.db import Base

from sqlalchemy import Column, String, relationship, ForeignKey
from sqlalchemy.dialects.postgresql import UUID



class Website(Base):
    __tablename__ = 'news_website'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    url = Column(String(200), unique=True)
    name = Column(String(100))

    articles = relationship("Article", back_populates="website")


class Article(Base):
    __tablename__ = 'news_article'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    url = Column(String(200))
    website_id = Column(UUID(as_uuid=True), ForeignKey("news_website.id"))
    text = Column(String(200))

    website = relationship('Website', foreign_keys='Article.website_id')
    entities = relationship(
        "Entity", secondary=ArticlesEntities, back_populates="articles"
    )


class ArticlesEntities(Base):
    __tablename__ = 'news_articles_entities'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    article_id = Column(UUID(as_uuid=True), ForeignKey("news_article.id"))
    entity_id = Column(UUID(as_uuid=True), ForeignKey("entities_entity.id"))
