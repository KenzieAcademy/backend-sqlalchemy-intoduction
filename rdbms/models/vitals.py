from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.exc import IntegrityError

from .database import Base, session
from .users import Users


class Vitals(Base):
    """
    vitals (id, user_id, height, weight
    """
    __tablename__ = 'vitals'

    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(ForeignKey('users.id'))
    height = Column(Integer())
    weight = Column(Integer())

    def __init__(self, **kwargs):
        super(Vitals, self).__init__(**kwargs)

    @staticmethod
    def _bootstrap(count=10, locale='en'):
        from mimesis import Person
        person = Person(locale)
        q = session.query(Users).all()
        for user in q:
            for _ in range(count):
                vital = Vitals(
                    user_id=user.id,
                    height=person.height(),
                    weight=person.weight()
                )
                session.add(vital)
                try:
                    session.commit()
                except IntegrityError:
                    session.rollback()
