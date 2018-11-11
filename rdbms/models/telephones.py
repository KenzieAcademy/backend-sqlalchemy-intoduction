from manage import Base
from sqlalchemy import Column, Integer, ForeignKey


class Telephones(Base):
    __tablename__ = 'telephones'

    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    telephone_number = Column(Integer, nullable=False)

