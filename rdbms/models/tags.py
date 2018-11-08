from sqlalchemy import Column, Integer, String, ForeignKey

from rdbms.models.database import Base

# CREATE TABLE tags (
# 	id INTEGER NOT NULL,
# 	user_id INTEGER,
# 	body VARCHAR(50),
# 	PRIMARY KEY (id),
# 	FOREIGN KEY(user_id) REFERENCES users (id)
# )


class Tag(Base):

    __tablename__ = 'tags'

    id = Column(Integer, nullable=False, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    body = Column(String(50))
