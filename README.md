## Objectives
- Define and create a simple relational database.
- Apply concepts of relational data modeling using a database abstraction layer
to define database entities.
- Compare and contrast differences between writing raw SQL statements and generating
raw SQL statements using an object-oriented approach to database abstraction. 

## Introduction
After reading about relational data modeling and relational database management
systems, let’s define a relational database using the database abstraction layer
SQLAlchemy instead of writing SQL statements ourselves. Using a database
abstraction layer such as SQLAlchemy frees developers from much of the
undifferentiated heavy lifting of working with databases including handling
many of the differences among relational database management systems. Although
SQL is a standardized language, each relational database management systems
implements it differently, and each RDBMS offers different features, leading to
inconsistencies across relational database management systems. These differences
accumulate overtime causing different dialects of SQL to emerge including Oracle's
P/SQL and Microsoft's T/SQL most notably. Database abstraction hides these
implementation details from developers allowing them to concentrate on the
business logic of applications instead.

As a database abstraction, SQLAlchemy implements the object-relational mapper
(ORM) design pattern for transforming database entities to native objects and 
back again using an object-oriented approach that translates to raw SQL
statements. You do not have to write SQL statements yourself, but to be clear,
we are not avoiding SQL. To use ORMs such as SQLAlchemy effectively, it is
necessary to understand relational data modeling and SQL, but learning an ORM
is an alternate if not gentler approach to learning relational data management
than SQL itself for reasons that will hopefully become clearer in the
following example.


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

from .database import Base


class User(Base):
    """Table of user entities with inherited CRUD methods."""
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    
users = User.all()
```





## Readings
Each link corresponds to a titled section of the linked document. You are only
asked to read the respective section of each link, not the whole page.

### Database Configuration
1. [Engine Configuration](https://docs.sqlalchemy.org/en/latest/core/engines.html#engine-configuration)
2. [Connecting](https://docs.sqlalchemy.org/en/latest/orm/tutorial.html#connecting)
3. [Database URLs](https://docs.sqlalchemy.org/en/latest/core/engines.html#database-urls)
2. [Creating a Session](https://docs.sqlalchemy.org/en/latest/orm/tutorial.html#creating-a-session)
### Data Modeling
1. [Declaratitive Mapping](https://docs.sqlalchemy.org/en/latest/orm/mapping_styles.html#declarative-mapping)
2. [One to Many Relationships](https://docs.sqlalchemy.org/en/latest/orm/basic_relationships.html#one-to-many)
3. [Many to One Relationships](https://docs.sqlalchemy.org/en/latest/orm/basic_relationships.html#many-to-one)
4. [One to One Relationships](https://docs.sqlalchemy.org/en/latest/orm/basic_relationships.html#one-to-one)
5. [Many to Many Relationships](https://docs.sqlalchemy.org/en/latest/orm/basic_relationships.html#many-to-many)
6. [Many to Many Relationships and Association Objects](https://docs.sqlalchemy.org/en/latest/orm/basic_relationships.html#association-object)
7. [Building a Many To Many Relationship](https://docs.sqlalchemy.org/en/latest/orm/tutorial.html#orm-tutorial-many-to-many)


## Instructions
1. Complete the readings.
2. Fork this repository and checkout a new branch to be merged with the existing
grading branch.
3. Define functions to configure and instantiate instances of the Engine, Session,
and Base classes as described in the Database Configuration section of the readings.
All configuration including database urls should be specified in environment variables.
4. Translate the following SQL table creation statements into SQLAlchemy models
following the declarative mapping style from the readings. Each model should be
in its own module within the models package, and each model should be importable
directly from the models package.
5. Run python manage.py init from the repository's root directory to create the
relational database defined by your models.
6. Commit your changes including an SQLite database created from your models,
then submit a pull request to complete the assignment.


```sql
CREATE TABLE users (
	id INTEGER NOT NULL, 
	username VARCHAR(20), 
	PRIMARY KEY (id)
)
```

```sql
CREATE TABLE posts (
	id INTEGER NOT NULL, 
	user_id INTEGER, 
	title VARCHAR(255), 
	body TEXT, 
	PRIMARY KEY (id), 
 	FOREIGN KEY(user_id) REFERENCES users (id)
)
```

```sql
CREATE TABLE comments (
	id INTEGER NOT NULL, 
	user_id INTEGER, 
	body TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(user_id) REFERENCES users (id)
)
```

```sql
CREATE TABLE tags (
	id INTEGER NOT NULL, 
	user_id INTEGER, 
	body VARCHAR(50), 
	PRIMARY KEY (id), 
	FOREIGN KEY(user_id) REFERENCES users (id)
)
```


```sql

```
# General Information

This program sets up a SQL database using SQLAlchemy. In this iteration, it creates a SQLite db file with all tables defined by the ORM.