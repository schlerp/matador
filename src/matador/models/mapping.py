from matador.models.base import MatadorMixin
from matador.persist.database import Base
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship


class Mapping(MatadorMixin, Base):
    """A mapping describes a simple transformation from one value to another."""

    __tablename__ = "mappings"

    codeset_name = Column(String)
    value_in = Column(String)
    value_out = Column(String)
    attribute_encodings = relationship("AttributeEncoding", back_populates="mapping")
