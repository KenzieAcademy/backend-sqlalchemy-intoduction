from manage import Base
from sqlalchemy import Column, Integer, ForeignKey


class Vitals(Base):
    __tablename__ = 'vitals'

    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    height = Column(Integer, nullable=False)
    weight = Column(Integer, nullable=False)
