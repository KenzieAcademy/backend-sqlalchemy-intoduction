from sqlalchemy import Column, Integer, String, ForeignKey

from .database import Base


class Tags(Base):
    """
    Emulates the following SQL statement:

    CREATE TABLE tags (
        id INTEGER NOT NULL,
        user_id INTEGER,
        body VARCHAR(50),
        PRIMARY KEY (id),
        FOREIGN KEY(user_id) REFERENCES users (id)
    )
    """
    __tablename__ = 'tags'

    id = Column(Integer, nullable=False, primary_key=True)
    user_id = Column(ForeignKey('users.id'))
    body = Column(String(50))
