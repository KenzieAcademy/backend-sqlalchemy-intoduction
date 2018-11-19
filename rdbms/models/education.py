from sqlalchemy import Column, Integer, String, ForeignKey
from .database import Base, session
from sqlalchemy.exc import IntegrityError
from .users import Users

class Education(Base):
    __tablename__ = 'education'
    id = Column(Integer, primary_key=True)
    user_id = Column(String, ForeignKey('user.id'))
    school = Column(String)
    start_date = Column(String)
    end_date = Column(String)
    graduated = Column(String)
    gpa = Column(Integer)

    @staticmethod
    def _bootstrap(count=10, locale='en'):
        from mimesis import Person, Datetime, Numbers, Development

        person = Person(locale)
        datetime = Datetime()
        number = Numbers()
        development = Development()
        all_users = session.query(Users).all()

        for user in all_users:
            education = Education(
                user_id = user.id,
                school = person.university(),
                start_date = datetime.date(start=2000, end=2002),
                end_date = datetime.date(start=2002, end=2018),
                graduated = development.boolean(),
                gpa = number.rating(maximum=4.0)
            )
            session.add(education)
            try:
                session.commit()
            except IntegrityError as err:
                session.rollback() 