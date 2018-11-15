from sqlalchemy import Column, Integer, String, ForeignKey
from .database import Base, session
from sqlalchemy.exc import IntegrityError
from .users import Users

class Posts(Base):
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True)
    user_id = Column(String, ForeignKey('user.id'))
    title = Column(String)
    body = Column(String)

    @staticmethod
    def _bootstrap(count=10, locale='en'):
        from mimesis import Text
        text = Text(locale)
        all_users = session.query(Users).all()

        for user in all_users:
            post = Posts(
                user_id=user.id,
                title=text.swear_word(),
                body=text.text(quantity=3)
            )
            session.add(post)
            try:
                session.commit()
            except IntegrityError as e:
                session.rollback()
