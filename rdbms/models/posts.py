from sqlalchemy import Column, Integer, String, ForeignKey, Text

from .database import Base


class Posts(Base):
    """
    Emulates the following SQL statement:

    CREATE TABLE posts(
        id INTEGER NOT NULL,
        user_id INTEGER,
        title VARCHAR(255),
        body TEXT,
        PRIMARY KEY(id),
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
    """
    __tablename__ = 'posts'

    id = Column(Integer, nullable=False, primary_key=True)
    user_id = Column(ForeignKey('users.id'))
    title = Column(String(255))
    body = Column(Text)
