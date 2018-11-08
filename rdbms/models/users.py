from sqlalchemy import Column, Integer, String

from .database import Base

class Users(Base):
    """CREATE TABLE users (
	id INTEGER NOT NULL, 
	username VARCHAR(20), 
	PRIMARY KEY (id)
    )"""
    __tablename__='users'

    id = Column(Integer, nullable=False, primary_key=True)
    username = Column(String(20))