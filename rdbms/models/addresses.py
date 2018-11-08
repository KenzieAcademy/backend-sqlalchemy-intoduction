from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.exc import IntegrityError

from .database import Base
from .database import session
from .users import Users

class Addresses(Base):

    __tablename__='addresses'

    id = Column(Integer, nullable=False, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    street_address_1 = Column(Text)
    street_address_2 = Column(Text)
    city = Column(Text)
    state = Column(Text)
    postal_code = Column(Text)
    country = Column(Text)
    start_date = Column(Text)
    end_date = Column(Text)

    def __init__(self, **kwargs):
        super(Addresses, self).__init__(**kwargs)

    @staticmethod
    def _bootstrap(count=50, locale='en'):
        from mimesis import Address, Datetime
        address = Address(locale)
        date = Datetime()
        que = session.query(Users)
        for user in que.all():
            for _ in range(10):
                addresses = Addresses(
                    user_id=user.id,
                    street_address_1=address.address(),
                    street_address_2=address.address(),
                    city=address.city(),
                    state=address.state(),
                    postal_code=address.postal_code(),
                    country=address.country(),
                    start_date=date.date(start=2000, end=2015),
                    end_date=date.date(start=2016, end=2019)
                )


                session.add(addresses)
                try:
                    session.commit()
                except IntegrityError:
                    session.rollback()