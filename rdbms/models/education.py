from sqlalchemy import Column, Integer, String, ForeignKey

from rdbms.models.database import Base


class Education(Base):
    __tablename__ = 'education'

    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey('users.id'))
    school = Column(String(40), nullable=False)
    start_date = Column(String(8), nullable=False)
    end_date = Column(String(8))
    graduated = Column(String)
    gpa = Column(Integer)
