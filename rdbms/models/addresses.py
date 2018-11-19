from sqlalchemy import Column, Integer, String, ForeignKey
from .database import Base, session
from sqlalchemy.exc import IntegrityError
from .users import Users
class Addresses(Base):
    __tablename__ = 'addresses'

    id = Column(Integer, primary_key=True)
    user_id = Column(String, ForeignKey('user.id'))
    street_address = Column(String)
    street_address_two = Column(String)
    city = Column(String)
    state = Column(String)
    postal_code = Column(String)
    country = Column(String)
    start_date = Column(String)
    end_date = Column(String)

    @staticmethod
    def _bootstrap(count=10, locale='en'):
        from mimesis import Text, Person, Address, Datetime
        text = Text(locale)
        person = Person(locale)
        addresses = Address()
        datetime = Datetime()
        all_users = session.query(Users).all()

        for user in all_users:
            address = Addresses(
                user_id = user.id,
                street_address = addresses.address(),
                street_address_two = addresses.street_number(),
                city = addresses.city(),
                state = addresses.state(),
                postal_code = addresses.postal_code(),
                country = addresses.country(),
                start_date = datetime.date(start=2000, end=2002),
                end_date = datetime.date(start=2002, end=2018)
            )
            session.add(address)
            try:
                session.commit()
            except IntegrityError as err:
                session.rollback()