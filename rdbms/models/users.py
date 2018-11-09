from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship
from mimesis import Person

from rdbms.models.database import Session
from .database import Base


class User(Base):
    """Table of user entities with inherited CRUD methods."""
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    email_address = Column(String)
    account = relationship('Account')
    address = relationship('Address')
    education = relationship('Education')
    employment = relationship('Employment')
    languages = relationship('Language')
    profile = relationship('Profile')
    telephone = relationship('Telephone')
    vitals = relationship('Vitals')

    @staticmethod
    def _bootstrap(count=50, locale='en'):
        sess = Session()
        for _ in range(count):
            person = Person(locale)
            attributes = {
                'username': person.username(),
                'password': person.password(),
                'email_address': person.email()
            }
            user = User(**attributes)
            sess.add(user)
        sess.commit()
