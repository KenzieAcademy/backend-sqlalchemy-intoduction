from manage import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class Languages(Base):
    __tablename__ = 'languages'

    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    language = Column(String(20), nullable=False)
