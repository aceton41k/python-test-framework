from pydantic import BaseModel


class Status(BaseModel):
    verified: bool
    sentCount: int
