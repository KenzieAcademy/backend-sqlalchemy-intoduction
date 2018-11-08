import os

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

db_url = os.getenv('db_url')


def make_engine(db=db_url):
    engine = create_engine(db)
    return engine

Base = declarative_base()

engine = make_engine()