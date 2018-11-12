from sqlalchemy import Column, Integer, String, ForeignKey

from rdbms.models.database import Base


class Employment(Base):
    __tablename__ = 'employments'

    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey('users.id'))
    company = Column(String(40), nullable=False)
    occupation = Column(String)
    start_date = Column(String(8), nullable=False)
    end_date = Column(String(8))
