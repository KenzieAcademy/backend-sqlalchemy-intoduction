from sqlalchemy import Column, Integer, String, ForeignKey
from .database import Base

class Tags(Base):
    __tablename__ = 'tag'

    id = Column(Integer, primary_key=True)
    user_id = Column(String, ForeignKey('user.id'))
    body = Column(String)