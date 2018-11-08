from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.exc import IntegrityError

from .database import Base
from .database import session
from .users import Users

class Accounts(Base):

    __tablename__='accounts'

    id = Column(Integer, nullable=False, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    social_media = Column(Text)

    def __init__(self, **kwargs):
        super(Accounts, self).__init__(**kwargs)

    @staticmethod
    def _bootstrap(count=50, locale='en'):
        from mimesis import Person
        person = Person(locale)
        que = session.query(Users)
        for user in que.all():
            for _ in range(10):
                accounts = Accounts(
                    user_id=user.id,
                    social_media=person.social_media_profile()
                )


                session.add(accounts)
                try:
                    session.commit()
                except IntegrityError:
                    session.rollback()