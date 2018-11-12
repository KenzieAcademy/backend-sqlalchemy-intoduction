from sqlalchemy import Column, Integer, ForeignKey

from rdbms.models.database import Base


class Vital(Base):
    __tablename__ = 'vital'

    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey('users.id'))
    height = Column(Integer, nullable=False)
    weight = Column(Integer, nullable=False)
