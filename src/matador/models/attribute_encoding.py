from matador.models.base import MatadorMixin
from matador.persist.database import Base
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship


class AttributeEncoding(MatadorMixin, Base):
    """An attribute encoding descibes how a dataset will be serialised,
    these are expressed at the attribute level."""

    __tablename__ = "attribute_encodings"

    dataset_id = Column(Integer, ForeignKey("datasets.id"))
    dataset = relationship("Dataset", back_populates="attribute_encodings")

    attribute_id = Column(Integer, ForeignKey("attributes.id"))
    attribute = relationship("Attribute", back_populates="attribute_encoding")

    mapping_id = Column(Integer, ForeignKey("mappings.id"))
    mapping = relationship("Mapping", back_populates="attribute_encodings")

    path = Column(String)
