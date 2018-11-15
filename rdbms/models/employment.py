from sqlalchemy import Column, Integer, String, ForeignKey
from .database import Base, session
from sqlalchemy.exc import IntegrityError
from .users import Users

class Employments(Base):
    __tablename__ = 'employment'

    id = Column(Integer, primary_key=True)
    user_id = Column(String, ForeignKey('user.id'))
    company = Column(String)
    occupation = Column(String)
    start_date = Column(String)
    end_date = Column(String)


    @staticmethod
    def _bootstrap(count=10, locale='en'):
        from mimesis import Person, Datetime, Business
        person = Person(locale)
        datetime = Datetime()
        business = Business()
        all_users = session.query(Users).all()

        for user in all_users:
            employment = Employments(
                user_id = user.id,
                company = business.company(),
                occupation = person.occupation(),
                start_date = datetime.date(start=2000, end=2002),
                end_date = datetime.date(start=2002, end=2018)
            )
            session.add(employment)
            try:
                session.commit()
            except IntegrityError as e:
                session.rollback()