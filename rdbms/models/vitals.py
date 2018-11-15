from sqlalchemy import Column, Integer, String, ForeignKey
from .database import Base, session
from sqlalchemy.exc import IntegrityError
from .users import Users

class Vitals(Base):
    __tablename__ = 'vitals'

    id = Column(Integer, primary_key=True)
    user_id = Column(String, ForeignKey('user.id'))
    height = Column(String)
    weight = Column(String)

    @staticmethod
    def _bootstrap(count=10, locale='en'):
        from mimesis import Text
        text = Text(locale)
        all_users = session.query(Users).all()

        for user in all_users:
            vitals = Vitals(
                user_id=user.id,
                height=text.text(quantity=1),
                weight=text.vitals(quantity=1)
            )
            session.add(vitals)
            try:
                session.commit()
            except IntegrityError as e:
                session.rollback()