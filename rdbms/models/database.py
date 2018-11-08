import os

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url = os.getenv('db_url', 'sqlite:///test.db')


def make_engine(db=db_url):
    engine = create_engine(db)
    return engine

Session = sessionmaker(bind=make_engine().connect())

session = Session()

Base = declarative_base()

engine = make_engine()
