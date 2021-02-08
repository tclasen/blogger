from datetime import datetime
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class Post(BaseModel):
    uuid: UUID = Field(default_factory=uuid4)
    title: str
    content: str
    created: datetime = Field(default_factory=datetime.utcnow)
