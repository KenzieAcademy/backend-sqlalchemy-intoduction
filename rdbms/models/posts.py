from sqlalchemy import Column, Integer, String, ForeignKey

from rdbms.models.database import Base


# CREATE TABLE posts (
# 	id INTEGER NOT NULL,
# 	user_id INTEGER,
# 	title VARCHAR(255),
# 	body TEXT,
# 	PRIMARY KEY (id),
#  	FOREIGN KEY(user_id) REFERENCES users (id)
# )

class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    title = Column(String(255))
    body = Column(String)
