from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()

class Tag(Base):
    __tablename__ = 'tag'

    id = Column(Integer, primary_key=True)
    tag = Column(String)