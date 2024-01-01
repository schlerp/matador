from matador.schemas.attribute_encoding import AttributeEncodingOut
from matador.schemas.base import BaseSchema
from matador.schemas.dataset import DatasetOut
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
    attribute_encoding: AttributeEncodingOut
    dataset_id: int
    dataset: DatasetOut
