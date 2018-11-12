from sqlalchemy import Column, Integer, String, ForeignKey

from rdbms.models.database import Base


class Language(Base):
    __tablename__ = 'languages'

    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey('users.id'))
    language = Column(String(40), nullable=False)
