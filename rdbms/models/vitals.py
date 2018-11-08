from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.exc import IntegrityError

from .database import Base
from .database import session
from .users import Users

class Vitals(Base):

    __tablename__='vitals'

    id = Column(Integer, nullable=False, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    height = Column(Text)
    weight = Column(Text)
    

    def __init__(self, **kwargs):
        super(Vitals, self).__init__(**kwargs)

    @staticmethod
    def _bootstrap(count=50, locale='en'):
        from mimesis import Person
        person = Person(locale)
        que = session.query(Users)
        for user in que.all():
            for _ in range(10):
                vitals = Vitals(
                    user_id=user.id,
                    height=person.height(),
                    weight=person.weight()
                )


                session.add(vitals)
                try:
                    session.commit()
                except IntegrityError:
                    session.rollback()