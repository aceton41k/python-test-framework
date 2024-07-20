from pydantic import BaseModel, Field


class Activity(BaseModel):
    activity: str
    type: str
    participants: int
    price: float = Field(gt=0)
    link: str
    key: int
    accessibility: float
