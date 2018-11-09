from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import DateTime
from mimesis import Person
from mimesis import Business
from mimesis import Datetime

from rdbms.models.database import Session

from .database import Base


class Employment(Base):
    __tablename__ = 'employments'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    company = Column(String)
    occupation = Column(String)
    start_date = Column(DateTime)
    end_date = Column(DateTime)

    @staticmethod
    def _bootstrap(user, count=10, locale='en'):
        sess = Session()
        for _ in range(count):
            person = Person(locale)
            business = Business(locale)
            datetime = Datetime()
            attributes = {
                'user_id': user.id,
                'company': business.company(),
                'occupation': person.occupation(),
                'start_date': datetime.datetime(),
                'end_date': datetime.datetime()
            }
            employment = Employment(**attributes)
            sess.add(employment)
        sess.commit()
