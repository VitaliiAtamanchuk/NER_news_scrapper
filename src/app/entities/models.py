import uuid

from app.core.db import Base

from sqlalchemy import Column, String, relationship
from sqlalchemy.dialects.postgresql import UUID

from app.news.models import ArticlesEntities



class Entity(Base):
    __tablename__ = 'entities_entity'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    text = Column(String(200)) # TODO: how long?
    label = Column(String(100)) # TODO: choice (1, 'LABEL')

    articles = relationship(
        "Articles", secondary=ArticlesEntities, back_populates="entities"
    )
