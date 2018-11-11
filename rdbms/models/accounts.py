from sqlalchemy import Column, Integer, ForeignKey, Text
from sqlalchemy.exc import IntegrityError

from .database import Base, session
from .users import Users


class Accounts(Base):
    """
    accounts (id, user_id, url
    """
    __tablename__ = 'accounts'

    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(ForeignKey('users.id'))
    url = Column(Text())

    def __init__(self, **kwargs):
        super(Accounts, self).__init__(**kwargs)

    @staticmethod
    def _bootstrap(count=10, locale='en'):
        from mimesis import Internet
        internet = Internet(locale)
        q = session.query(Users).all()
        for user in q:
            for _ in range(count):
                acct = Accounts(
                    user_id=user.id,
                    url=internet.home_page()
                )
                session.add(acct)
                try:
                    session.commit()
                except IntegrityError:
                    session.rollback()
