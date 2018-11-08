from sqlalchemy import Column, Integer, String

from rdbms.models.database import Base

# CREATE TABLE users (
# 	id INTEGER NOT NULL,
# 	username VARCHAR(20),
# 	PRIMARY KEY (id)
# )


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String(20), unique=True, nullable=False)

