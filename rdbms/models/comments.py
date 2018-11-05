from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from .database import Base


class Comment(Base):
    """Table of comments"""
    __tablename__ = 'columns'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    text = Column(String)
    user = relationship('User', back_populates='comments')
