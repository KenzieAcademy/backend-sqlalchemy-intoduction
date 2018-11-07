from manage import Base
from sqlalchemy import Column, Integer, String, Text, ForeignKey


class Posts(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    title = Column(String(255))
    body = Column(Text)
