from sqlalchemy import Column, Integer, String
from sqlalchemy.exc import IntegrityError

from .database import Base, session


class Users(Base):
    """
    users (id, username, password, email_address
    """
    __tablename__ = 'users'

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    username = Column(String(20), nullable=False, unique=True)
    password = Column(String(300), nullable=False)
    email_address = Column(String(320), nullable=False)

    def __init__(self, **kwargs):
        super(Users, self).__init__(**kwargs)

    @staticmethod
    def _bootstrap(count=50, locale='en'):
        from mimesis import Person
        p = Person(locale)
        for _ in range(count):
            user = Users(
                username=p.username(),
                password=p.password(),
                email_address=p.email()
            )
            session.add(user)
            try:
                session.commit()
            except IntegrityError:
                session.rollback()
