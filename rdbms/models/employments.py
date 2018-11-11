from sqlalchemy import Column, Integer, ForeignKey, Text
from sqlalchemy.exc import IntegrityError

from .database import Base, session
from .users import Users


class Employments(Base):
    """
    employments (id, user_id, company, occupation, start_date, end_date
    """
    __tablename__ = 'employments'

    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(ForeignKey('users.id'))
    company = Column(Text())
    occupation = Column(Text())
    start_date = Column(Text())
    end_date = Column(Text())

    def __init__(self, **kwargs):
        super(Employments, self).__init__(**kwargs)

    @staticmethod
    def _bootstrap(count=10, locale='en'):
        from mimesis import Person, Datetime, Business
        person = Person(locale)
        q = session.query(Users).all()
        for user in q:
            for _ in range(count):
                employment = Employments(
                    user_id=user.id,
                    company=Business().company(),
                    occupation=person.occupation(),
                    start_date=Datetime().date(start=2005, end=2015),
                    end_date=Datetime().date(start=2016, end=2018)
                )
                session.add(employment)
                try:
                    session.commit()
                except IntegrityError:
                    session.rollback()
