from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.exc import IntegrityError

from .database import Base
from .database import session
from .users import Users

class Employment(Base):

    __tablename__='employment'

    id = Column(Integer, nullable=False, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    occupation = Column(Text)
    company = Column(Text)
    start_date = Column(Text)
    end_date = Column(Text)
    

    def __init__(self, **kwargs):
        super(Employment, self).__init__(**kwargs)

    @staticmethod
    def _bootstrap(count=50, locale='en'):
        from mimesis import Datetime, Person, Business
        person = Person(locale)
        date = Datetime()
        business = Business()
        que = session.query(Users)
        for user in que.all():
            for _ in range(10):
                employment = Employment(
                    user_id=user.id,
                    occupation=person.occupation(),
                    company=business.company(),
                    start_date=date.date(start=2000, end=2015),
                    end_date=date.date(start=2016, end=2019)
                )


                session.add(employment)
                try:
                    session.commit()
                except IntegrityError:
                    session.rollback()