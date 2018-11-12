from sqlalchemy import Column, Integer, String, ForeignKey

from rdbms.models.database import Base


class Profile(Base):
    __tablename__ = 'profiles'

    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey('users.id'))
    nationality = Column(String(40), nullable=False)
