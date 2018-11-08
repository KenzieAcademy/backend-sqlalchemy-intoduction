from sqlalchemy import Column, Integer, String, ForeignKey

from rdbms.models.database import Base

# CREATE TABLE comments (
# 	id INTEGER NOT NULL,
# 	user_id INTEGER,
# 	body TEXT,
# 	PRIMARY KEY (id),
# 	FOREIGN KEY(user_id) REFERENCES users (id)
# )


class Comment(Base):

    __tablename__ = 'comments'

    id = Column(Integer, nullable=False, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    body = Column(String)
