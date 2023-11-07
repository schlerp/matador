from matador.schemas.base import BaseSchema
from pydantic import BaseModel


class DatasetBase(BaseModel):
    """Base class for dataset schemas."""

    name: str
    type: str
    owner: str


class DatasetIn(BaseSchema, DatasetBase):
    pass


class DatasetOut(BaseSchema, DatasetBase):
    attributes: list["Attributes"]
    attribute_encodings: list["AttributeEncodings"]
