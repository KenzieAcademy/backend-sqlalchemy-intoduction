from sqlalchemy import Column, Integer, String, ForeignKey

from rdbms.models.database import Base


class Tag(Base):

    __tablename__ = 'tags'

    id = Column(Integer, nullable=False, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    body = Column(String(50))
