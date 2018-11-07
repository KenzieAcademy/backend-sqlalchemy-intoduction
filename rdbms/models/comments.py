from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()

class Message(Base):
    __tablename__ = 'message'

    id = Column(Integer, primary_key=True)
    message = Column(String)
    time_created = Column(Integer)