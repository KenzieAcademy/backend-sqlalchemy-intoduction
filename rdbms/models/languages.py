from sqlalchemy import Column, Integer, ForeignKey, Text
from sqlalchemy.exc import IntegrityError

from .database import Base, session
from .users import Users


class Languages(Base):
    """
    languages (id, user_id, language
    """
    __tablename__ = 'languages'

    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(ForeignKey('users.id'))
    language = Column(Text)

    def __init__(self, **kwargs):
        super(Languages, self).__init__(**kwargs)

    @staticmethod
    def _bootstrap(count=10, locale='en'):
        from mimesis import Person
        person = Person(locale)
        q = session.query(Users).all()
        for user in q:
            for _ in range(count):
                language = Languages(
                    user_id=user.id,
                    language=person.language()
                )
                session.add(language)
                try:
                    session.commit()
                except IntegrityError:
                    session.rollback()
