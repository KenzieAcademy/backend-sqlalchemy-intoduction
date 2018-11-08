from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.exc import IntegrityError

from .database import Base
from .database import session
from .users import Users

class Profiles(Base):

    __tablename__='profiles'

    id = Column(Integer, nullable=False, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    profiles = Column(Text)
    

    def __init__(self, **kwargs):
        super(Profiles, self).__init__(**kwargs)

    @staticmethod
    def _bootstrap(count=50, locale='en'):
        from mimesis import Person
        person = Person(locale)
        que = session.query(Users)
        for user in que.all():
            for _ in range(10):
                profiles = Profiles(
                    user_id=user.id,
                    profiles=person.nationality()
                )


                session.add(profiles)
                try:
                    session.commit()
                except IntegrityError:
                    session.rollback()