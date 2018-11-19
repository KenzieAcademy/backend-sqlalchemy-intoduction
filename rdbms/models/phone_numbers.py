from sqlalchemy import Column, Integer, String, ForeignKey
from .database import Base, session
from sqlalchemy.exc import IntegrityError
from .users import Users

class Telephones(Base):
    __tablename__ = 'telephone number'

    id = Column(Integer, primary_key=True)
    user_id = Column(String, ForeignKey('user.id'))
    telephone_number = Column(Integer)

    @staticmethod
    def _bootstrap(count=10, locale='en'):
        from mimesis import Person
        person = Person(locale)
        all_users = session.query(Users).all()

        for user in all_users:
            telephone = Telephones(
                user_id=user.id,
                telephone_number=person.telephone(mask='', placeholder='#')
            )
            session.add(telephone)
            try:
                session.commit()
            except IntegrityError as err:
                session.rollback()