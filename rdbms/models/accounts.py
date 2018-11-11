from manage import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class Accounts(Base):
    __tablename__ = 'accounts'

    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    social_media_url = Column(String(20), nullable=False)
