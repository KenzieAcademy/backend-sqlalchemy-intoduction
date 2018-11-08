from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.exc import IntegrityError

from .database import Base
from .database import session

class Users(Base):
    """CREATE TABLE users (
	id INTEGER NOT NULL, 
	username VARCHAR(20), 
	PRIMARY KEY (id)
    )"""
    __tablename__='users'

    id = Column(Integer, nullable=False, primary_key=True)
    username = Column(String(20))
    password = Column(Text)
    email_address = Column(Text)

    def __init__(self, **kwargs):
        super(Users, self).__init__(**kwargs)

    @staticmethod
    def _bootstrap(count=50, locale='en'):
        from mimesis import Person
        person = Person(locale)

        for _ in range(count):
            user = Users(
                username=person.full_name(),
                password=person.password(),
                email_address=person.email()
            )

            session.add(user)
            try:
                session.commit()
            except IntegrityError:
                session.rollback()

