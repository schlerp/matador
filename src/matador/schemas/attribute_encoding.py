from pydantic import BaseModel
from matador.schemas.base import BaseSchema


class AttributeEncodingBase(BaseModel):
    """Base class for attribute encoding schemas."""

    dataset_id: int
    attribute_id: int
    mapping_id: int
    path: str


class AttributeEncodingIn(AttributeEncodingBase, BaseSchema):
    pass


class AttributeEncodingOut(AttributeEncodingBase, BaseSchema):
    dataset: "Dataset"
    attribute: "Attribute"
    mapping: "Mapping"
