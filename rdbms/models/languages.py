from sqlalchemy import Column, Integer, String, ForeignKey
from .database import Base, session
from sqlalchemy.exc import IntegrityError
from .users import Users

class Languages(Base):
    __tablename__ = 'language'

    id = Column(Integer, primary_key=True)
    user_id = Column(String, ForeignKey('user.id'))
    language = Column(String)

    @staticmethod
    def _bootstrap(count=10, locale='en'):
        from mimesis import Person
        person = Person(locale)
        all_users = session.query(Users).all()

        for user in all_users:
            language = Languages(
                user_id=user.id,
                language=person.language()
            )
            session.add(language)
            try:
                session.commit()
            except IntegrityError as e:
                session.rollback()