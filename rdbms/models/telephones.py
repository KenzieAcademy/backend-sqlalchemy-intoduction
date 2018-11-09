from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import ForeignKey
from mimesis import Person

from rdbms.models.database import Session

from .database import Base


class Telephone(Base):
    __tablename__ = 'telephones'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    telephone = Column(Integer)

    @staticmethod
    def _bootstrap(user, count=10, locale='en'):
        sess = Session()
        for _ in range(count):
            person = Person(locale)
            attributes = {
                'user_id': user.id,
                'telephone': person.telephone()
            }
            telephone = Telephone(**attributes)
            sess.add(telephone)
        sess.commit()
