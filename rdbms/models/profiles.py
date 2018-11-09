from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from mimesis import Person

from rdbms.models.database import Session

from .database import Base


class Profile(Base):
    __tablename__ = 'profiles'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    nationality = Column(String)

    @staticmethod
    def _bootstrap(user, count=10, locale='en'):
        sess = Session()
        for _ in range(count):
            person = Person(locale)
            attributes = {
                'user_id': user.id,
                'nationality': person.nationality()
            }
            profile = Profile(**attributes)
            sess.add(profile)
        sess.commit()
