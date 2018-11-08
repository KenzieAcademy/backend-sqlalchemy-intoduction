from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.exc import IntegrityError

from .database import Base
from .database import session
from .users import Users

class Telephones(Base):

    __tablename__='telephones'

    id = Column(Integer, nullable=False, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    telephones = Column(Text)
    

    def __init__(self, **kwargs):
        super(Telephones, self).__init__(**kwargs)

    @staticmethod
    def _bootstrap(count=50, locale='en'):
        from mimesis import Person
        person = Person(locale)
        que = session.query(Users)
        for user in que.all():
            for _ in range(10):
                telephones = Telephones(
                    user_id=user.id,
                    telephones=person.telephone()
                )


                session.add(telephones)
                try:
                    session.commit()
                except IntegrityError:
                    session.rollback()