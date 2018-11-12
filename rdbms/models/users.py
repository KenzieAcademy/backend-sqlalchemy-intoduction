from sqlalchemy import Column, Integer, String

from rdbms.models.database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String(30), unique=True, nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(40), nullable=False)
