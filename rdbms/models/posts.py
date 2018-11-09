from sqlalchemy import Column, Integer, String, ForeignKey
from .database import Base

class Posts(Base):
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True)
    user_id = Column(String, ForeignKey('user.id'))
    title = Column(String)
    body = Column(String)
