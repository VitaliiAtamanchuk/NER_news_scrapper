from uuid import uuid4, UUID

from pydantic import BaseModel, Field, HttpUrl

class WebsiteSchemaIn(BaseModel):
    name: str = Field(max_length=200)
    url: HttpUrl = Field(max_length=100)


class WebsiteSchemaOut(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str = Field(max_length=200)
    url: HttpUrl = Field(max_length=100)


class ArticleSchemaOut(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    url: HttpUrl = Field(max_length=100)
