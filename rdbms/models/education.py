from sqlalchemy import Column, Integer, ForeignKey, Text
from sqlalchemy.exc import IntegrityError

from .database import Base, session
from .users import Users


class Education(Base):
    """
    education (id, user_id, school, start_date, end_date, graduated, gpa
    """
    __tablename__ = 'education'

    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(ForeignKey('users.id'))
    school = Column(Text())
    start_date = Column(Text())
    end_date = Column(Text())
    graduated = Column(Text())
    gpa = Column(Text())

    def __init__(self, **kwargs):
        super(Education, self).__init__(**kwargs)

    @staticmethod
    def _bootstrap(count=10, locale='en'):
        import random
        from mimesis import Person, Datetime
        person = Person(locale)
        q = session.query(Users).all()
        for user in q:
            for _ in range(count):
                education = Education(
                    user_id=user.id,
                    school=person.university(),
                    start_date=Datetime().date(start=2005, end=2015),
                    end_date=Datetime().date(start=2016, end=2018),
                    graduated=Datetime().date(start=2016, end=2018),
                    gpa=random.choice([3.5, 4.0, 2.5, 3.0])
                )
                session.add(education)
                try:
                    session.commit()
                except IntegrityError:
                    session.rollback()
