from sqlalchemy import Column, Integer, String, ForeignKey
from .database import Base

class Users(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String)
