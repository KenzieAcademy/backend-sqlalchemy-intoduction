import random

from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.exc import IntegrityError

from .database import Base
from .database import session
from .users import Users

class Education(Base):

    __tablename__='education'

    id = Column(Integer, nullable=False, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    school = Column(Text)
    start_date = Column(Text)
    end_date = Column(Text)
    graduated = Column(Text)
    gpa = Column(Text)

    def __init__(self, **kwargs):
        super(Education, self).__init__(**kwargs)

    @staticmethod
    def _bootstrap(count=50, locale='en'):
        from mimesis import Datetime, Person, Numbers
        person = Person(locale)
        date = Datetime()
        number = Numbers()
        que = session.query(Users)
        for user in que.all():
            for _ in range(10):
                education = Education(
                    user_id=user.id,
                    start_date=date.date(start=2000, end=2015),
                    end_date=date.date(start=2016, end=2019),
                    school=person.university(),
                    graduated=random.choice(['yes', 'no']),
                    gpa=number.rating(maximum=4.0)
                )


                session.add(education)
                try:
                    session.commit()
                except IntegrityError:
                    session.rollback()