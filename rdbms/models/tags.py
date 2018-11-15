from sqlalchemy import Column, Integer, String, ForeignKey
from .database import Base, session
from sqlalchemy.exc import IntegrityError
from .users import Users

class Tags(Base):
    __tablename__ = 'tag'

    id = Column(Integer, primary_key=True)
    user_id = Column(String, ForeignKey('user.id'))
    body = Column(String)

    @staticmethod
    def _bootstrap(count=10, locale='en'):
        from mimesis import Text
        text = Text(locale)
        all_users = session.query(Users).all()

        for user in all_users:
            tag = Tags(
                user_id=user.id,
                body=text.text(quantity=1)
            )
            session.add(tag)
            try:
                session.commit()
            except IntegrityError as e:
                session.rollback()