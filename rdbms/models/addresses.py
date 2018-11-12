from sqlalchemy import Column, Integer, String, ForeignKey

from rdbms.models.database import Base


class Addr(Base):
    __tablename__ = 'addresses'

    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey('users.id'))
    street_address = Column(String(40), nullable=False)
    street_address_two = Column(String(40))
    city = Column(String(40), nullable=False)
    state = Column(String(20), nullable=False)
    postal_code = Column(Integer, nullable=False)
    country = Column(String(40), nullable=False)
    start_date = Column(String(8), nullable=False)
    end_date = Column(String(8))
