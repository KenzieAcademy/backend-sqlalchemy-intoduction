## sqlalchemy sprint a
- creates a simple relational database.
- Apply concepts of relational data modeling using a database abstraction layer
to define database entities.
- Compare and contrast differences between writing raw SQL statements and generating
raw SQL statements using an object-oriented approach to database abstraction. 

# use
run 'python manage.py init'


## Example
SQL table definition and query without database abstraction.
```python
import sqlite3

# SQL statements
SQL_CREATE_USERS_TABLE = """
CREATE TABLE users (
	id INTEGER NOT NULL, 
	username VARCHAR, 
	PRIMARY KEY (id)
);
"""
SQL_QUERY_USERS_TABLE = "SELECT * FROM users;"

# Creating database connection and cursor
db = sqlite3.connect("development.db")
cursor = db.cursor()

# Create table
cursor.execute(SQL_CREATE_USERS_TABLE)

# Query table
cursor.execute(SQL_QUERY_USERS_TABLE)

# Fetch Results
users = cursor.fetchall()
```
Equivalent table definition and query using database abstraction.
```python
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from .database import Base, session


class User(Base):
    """Table of user entities with inherited CRUD methods."""
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String)

users = session.query(User)
```


