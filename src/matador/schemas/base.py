import datetime

from pydantic import BaseModel


class BaseSchema(BaseModel):
    """The base schema for all other schemas to inherit from."""

    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime

    class Config:
        orm_mode = True
