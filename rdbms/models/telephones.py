from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.exc import IntegrityError

from .database import Base, session
from .users import Users


class Telephones(Base):
    """
    telephones (id, user_id, number
    """
    __tablename__ = 'telephones'

    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(ForeignKey('users.id'))
    number = Column(Integer)

    def __init__(self, **kwargs):
        super(Telephones, self).__init__(**kwargs)

    @staticmethod
    def _bootstrap(count=10, locale='en'):
        from mimesis import Person
        person = Person(locale)
        q = session.query(Users).all()
        for user in q:
            for _ in range(count):
                telephone = Telephones(
                    user_id=user.id,
                    number=person.telephone()
                )
                session.add(telephone)
                try:
                    session.commit()
                except IntegrityError:
                    session.rollback()
