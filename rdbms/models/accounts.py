from sqlalchemy import Column, Integer, String, ForeignKey
from .database import Base, session
from sqlalchemy.exc import IntegrityError
from .users import Users

class Accounts(Base):
    __tablename__ = 'account'
    id = Column(Integer, primary_key=True)
    user_id = Column(String, ForeignKey('user.id'))
    social_media_url = Column(String)

    @staticmethod
    def _bootstrap(count=10, locale='en'):
        from mimesis import Internet

        internet = Internet(locale)
        all_users = session.query(Users).all()

        for user in all_users:
            account = Accounts(
                user_id=user.id,
                social_media_url=internet.home_page()
            )
            session.add(account)

            try:
                session.commit()
            except IntegrityError as err:
                session.rollback() 