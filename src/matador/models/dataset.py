from matador.models.base import MatadorMixin
from matador.persist.database import Base
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship


class Dataset(MatadorMixin, Base):
    """A dataset is used to group a collection of attributes together."""

    __tablename__ = "datasets"

    name = Column(String, unique=True, index=True)
    type = Column(String)
    owner = Column(String)

    attributes = relationship("Attribute", back_populates="dataset")
    attribute_encodings = relationship("AttributeEncoding")
