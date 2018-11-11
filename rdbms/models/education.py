from manage import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float


class Education(Base):
    __tablename__ = 'education'

    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    school = Column(String(30), nullable=False)
    start_date = Column(Integer, nullable=False)
    end_date = Column(Integer, nullable=False)
    graduated = Column(String(30))
    gpa = Column(Float)
