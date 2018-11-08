from sqlalchemy import Column, Integer, ForeignKey, Text

from .database import Base


class Comments(Base):
    """CREATE TABLE comments (
	id INTEGER NOT NULL, 
	user_id INTEGER, 
	body TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(user_id) REFERENCES users (id)
    )"""

    __tablename__='comments'

    id = Column(Integer, nullable=False, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    body = Column(Text)