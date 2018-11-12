from sqlalchemy import Column, Integer, String, ForeignKey

from rdbms.models.database import Base


class Account(Base):
    __tablename__ = 'accounts'

    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey('users.id'))
    url = Column(String(20), unique=True, nullable=False)
