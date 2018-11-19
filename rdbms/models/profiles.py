from sqlalchemy import Column, Integer, String, ForeignKey
from .database import Base, session
from sqlalchemy.exc import IntegrityError
from .users import Users
class Profiles(Base):
    __tablename__ = 'profile'

    id = Column(Integer, primary_key=True)
    user_id = Column(String, ForeignKey('user.id'))
    nationality = Column(String)

    @staticmethod
    def _bootstrap(count=10, locale='en'):
        from mimesis import Person
        person = Person(locale)
        all_users = session.query(Users).all()

        for user in all_users:
            profile = Profiles(
                user_id=user.id,
                nationality=person.nationality()
            )
            session.add(profile)
            try:
                session.commit()
            except IntegrityError as err:
                session.rollback() 