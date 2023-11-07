from matador.schemas.base import BaseSchema
from pydantic import BaseModel


class MappingBase(BaseModel):
    """Base class for mapping schemas."""

    codeset_name: str
    value_in: str
    value_out: str


class MappingIn(BaseSchema, MappingBase):
    pass


class MappingOut(BaseSchema, MappingBase):
    attribute_encodings: list["AttributeEncodingOut"]
