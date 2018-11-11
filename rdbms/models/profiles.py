from manage import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class Profiles(Base):
    __tablename__ = 'profiles'

    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    nationality = Column(String(20), nullable=False)
