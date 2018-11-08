from sqlalchemy import Column, Integer, String, ForeignKey, Text

from .database import Base, session

from .users import Users


class Posts(Base):
    """CREATE TABLE posts (
	id INTEGER NOT NULL, 
	user_id INTEGER, 
	title VARCHAR(255), 
	body TEXT, 
	PRIMARY KEY (id), 
 	FOREIGN KEY(user_id) REFERENCES users (id)
    )"""

    __tablename__='posts'

    id = Column(Integer, nullable=False, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    title = Column(String(255))
    body = Column(Text)

    def __init__(self, **kwargs):
        super(Posts, self).__init__(**kwargs)

    @staticmethod
    def _bootstrap(count=50, locale='en'):
        from mimesis import Person, Text
        person = Person(locale)
        text = Text(locale)
        que = session.query(Users)
        for user in que.all():
            for post in range(10):
                posts = Posts(
                    user_id=user.id,
                    title=text.title(),
                    body=text.sentence()
                )


                session.add(posts)
                try:
                    session.commit()
                except IntegrityError:
                    session.rollback()