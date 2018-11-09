from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import DateTime
from mimesis import Person
from mimesis import Datetime
from mimesis import Numbers

from rdbms.models.database import Session

from .database import Base


class Education(Base):
    __tablename__ = 'education'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    school = Column(String)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    graduated = Column(String)
    gpa = Column(Integer)

    @staticmethod
    def _bootstrap(user, count=10, locale='en'):
        sess = Session()
        for _ in range(count):
            person = Person(locale)
            datetime = Datetime()
            gpa = Numbers()
            attributes = {
                'user_id': user.id,
                'school': person.university(),
                'start_date': datetime.datetime(),
                'end_date': datetime.datetime(),
                'graduated': person.academic_degree(),
                'gpa': gpa.between(minimum=1, maximum=4)
            }
            education = Education(**attributes)
            sess.add(education)
        sess.commit()
