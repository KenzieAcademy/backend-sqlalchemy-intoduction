from sqlalchemy import Column, Integer, ForeignKey, Text, String
from sqlalchemy.exc import IntegrityError

from .database import Base, session
from .users import Users


class Addresses(Base):
    """
    addresses (id, user_id, street_address, street_address_two, city, state, postal_code, country, start_date, end_date
    """
    __tablename__ = 'addresses'

    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(ForeignKey('users.id'))
    street_address = Column(String(100))
    street_address_two = Column(String(100))
    city = Column(String(50))
    state = Column(String(25))
    postal_code = Column(String(10))
    country = Column(Text())
    start_date = Column(Text())
    end_date = Column(Text())

    def __init__(self, **kwargs):
        super(Addresses, self).__init__(**kwargs)

    @staticmethod
    def _bootstrap(count=10, locale='en'):
        from mimesis import Address, Datetime
        address = Address(locale)
        q = session.query(Users).all()
        for user in q:
            for _ in range(count):
                a = Addresses(
                    user_id=user.id,
                    street_address=address.address(),
                    street_address_two=address.street_number(),
                    city=address.city(),
                    state=address.state(),
                    postal_code=address.postal_code(),
                    country=address.country(),
                    start_date=Datetime().date(start=2005, end=2015),
                    end_date=Datetime().date(start=2016, end=2018)
                )
                session.add(a)
                try:
                    session.commit()
                except IntegrityError:
                    session.rollback()
