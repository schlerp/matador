from matador.models.base import MatadorMixin
from matador.persist.database import Base
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship


class Attribute(MatadorMixin, Base):
    """An attribute represents a field of a dataset, or a column of a table."""

    __tablename__ = "attributes"

    name = Column(String)
    datatype = Column(String)
    optional = Column(Boolean)
    primary_key = Column(Boolean)

    attribute_encoding = relationship("AttributeEncoding", back_populates="attribute")

    dataset_id = Column(Integer, ForeignKey("Dataset"))
    dataset = relationship("Dataset", back_populates="attributes")
