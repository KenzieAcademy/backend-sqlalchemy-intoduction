from manage import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class Addresses(Base):
    __tablename__ = 'addresses'

    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    street_address = Column(String(50), nullable=False)
    street_address_two = Column(String(50), nullable=False)
    city = Column(String(20), nullable=False)
    state = Column(String(15), nullable=False)
    postal_code = Column(Integer, nullable=False)
    country = Column(String(20), nullable=False)
    start_date = Column(Integer, nullable=False)
    end_date = Column(Integer, nullable=False)
