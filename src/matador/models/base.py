import datetime

from sqlalchemy import Column, DateTime, Integer


class MatadorMixin(object):
    """A mixin for all Matador models."""

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(
        DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow
    )
