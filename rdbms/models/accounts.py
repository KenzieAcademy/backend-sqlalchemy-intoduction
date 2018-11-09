from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from mimesis import Person

from rdbms.models.database import Session

from .database import Base


class Account(Base):
    __tablename__ = 'accounts'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    social_media_url = Column(String)

    @staticmethod
    def _bootstrap(user, count=10, locale='en'):
        sess = Session()
        for _ in range(count):
            person = Person(locale)
            attributes = {
                'user_id': user.id,
                'social_media_url': person.social_media_profile(),
            }
            account = Account(**attributes)
            sess.add(account)
        sess.commit()
