from sqlalchemy import Column, Integer, ForeignKey, Text
from sqlalchemy.exc import IntegrityError

from .database import Base, session
from .users import Users


class Profiles(Base):
    """
    profiles (id, user_id, nationality
    """
    __tablename__ = 'profiles'

    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(ForeignKey('users.id'))
    nationality = Column(Text)

    def __init__(self, **kwargs):
        super(Profiles, self).__init__(**kwargs)

    @staticmethod
    def _bootstrap(count=10, locale='en'):
        from mimesis import Person
        person = Person(locale)
        q = session.query(Users).all()
        for user in q:
            for _ in range(count):
                profile = Profiles(
                    user_id=user.id,
                    nationality=person.nationality()
                )
                session.add(profile)
                try:
                    session.commit()
                except IntegrityError:
                    session.rollback()
