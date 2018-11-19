from sqlalchemy import Column, Integer, String, ForeignKey
from .database import Base


class Post(Base):
    """Table of user entities with inherited CRUD methods."""
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    title = Column(String)
    body = Column(String)


# posts = session.query(Post)