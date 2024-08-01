from pydantic import BaseModel, Field

from model.status import Status


class CatFact(BaseModel):
    status: Status
    id: str = Field(alias='_id')
    user: str
    text: str
    v: int = Field(alias='__v')
    source: str
    updated_at: str = Field(alias='updatedAt')
    type: str
    created_at: str = Field(alias='createdAt')
    deleted: bool
    used: bool
