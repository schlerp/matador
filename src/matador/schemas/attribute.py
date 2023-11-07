from matador.schemas.base import BaseSchema
from pydantic import BaseModel


class AttributeBase(BaseModel):
    """Base class for attribute schemas."""

    name: str
    datatype: str
    optional: bool
    primary_key: bool


class AttributeIn(AttributeBase, BaseSchema):
    pass


class AttributeOut(AttributeBase, BaseSchema):
    attribute_encoding: list["AttributeEncodingOut"]
    dataset_id: int
    dataset: "DatasetOut"
