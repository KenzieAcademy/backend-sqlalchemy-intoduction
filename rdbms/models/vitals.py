from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import ForeignKey
from sqlalchemy import String
from mimesis import Person

from rdbms.models.database import Session

from .database import Base


class Vitals(Base):
    __tablename__ = 'vitals'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    height = Column(String)
    weight = Column(String)

    @staticmethod
    def _bootstrap(user, count=10, locale='en'):
        sess = Session()
        for _ in range(count):
            person = Person(locale)
            attributes = {
                'user_id': user.id,
                'height': person.height(),
                'weight': person.weight()
            }
            vitals = Vitals(**attributes)
            sess.add(vitals)
        sess.commit()
