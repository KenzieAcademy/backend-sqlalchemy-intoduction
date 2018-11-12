from sqlalchemy import Column, Integer, String, ForeignKey

from rdbms.models.database import Base


class Comment(Base):

    __tablename__ = 'comments'

    id = Column(Integer, nullable=False, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    body = Column(String)
