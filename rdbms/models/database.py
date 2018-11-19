import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


db_url = os.getenv('DB_URL', 'sqlite:///knob.db')

engine = create_engine(db_url, echo = True)
connection = engine.connect()

Session = sessionmaker(bind=connection)
session = Session()

Base = declarative_base()
