from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.exc import IntegrityError
from .database import Base, session

class Users(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    
    @staticmethod
    def _bootstrap(count=50, locale='en'):
        from mimesis import Person
        person = Person(locale)

        for _ in range(count):
            user = Users(
                username=person.username(template=None)
            )
            session.add(user)
            try:
                session.commit()
            except IntegrityError as err:
                print(err)
                session.rollback()