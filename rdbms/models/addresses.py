from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import DateTime
from mimesis import Address as MimAddress
from mimesis import Datetime

from rdbms.models.database import Session

from .database import Base


class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    street_address = Column(String)
    street_address_two = Column(String)
    city = Column(String)
    state = Column(String)
    postal_code = Column(String)
    country = Column(String)
    start_date = Column(DateTime)
    end_date = Column(DateTime)

    @staticmethod
    def _bootstrap(user, count=10, locale='en'):
        sess = Session()
        for _ in range(count):
            gen_address = MimAddress(locale)
            datetime = Datetime(locale)
            attributes = {
                'user_id': user.id,
                'street_address': gen_address.street_number() + " " +
                gen_address.street_name(),
                'street_address_two': gen_address.street_number() + " " +
                gen_address.street_name(),
                'city': gen_address.city(),
                'state': gen_address.state(),
                'postal_code': gen_address.postal_code(),
                'country': gen_address.country(),
                'start_date': datetime.datetime(start=2000, end=2010),
                'end_date': datetime.datetime(start=2010)
            }
            address = Address(**attributes)
            sess.add(address)
        sess.commit()
