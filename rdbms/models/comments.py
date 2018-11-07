from manage import Base
from sqlalchemy import Column, Integer, Text, ForeignKey


class Comments(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    body = Column(Text)
