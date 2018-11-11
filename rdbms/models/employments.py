from manage import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class Employments(Base):
    __tablename__ = 'employments'

    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    company = Column(String(30), nullable=False)
    occupation = Column(String(20), nullable=False)
    start_date = Column(Integer, nullable=False)
    end_date = Column(Integer, nullable=False)
