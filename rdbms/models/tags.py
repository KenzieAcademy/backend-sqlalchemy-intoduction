from manage import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class Tags(Base):
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    body = Column(String(50))
