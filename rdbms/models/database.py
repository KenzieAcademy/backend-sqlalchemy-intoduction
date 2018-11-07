import os

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = os.getenv('DATABASE_URL')


def make_engine(database=DATABASE_URL):
    engine = create_engine(database)
    return engine


def make_base():
    Base = declarative_base()
    return Base


def make_session(engine):
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


engine = make_engine()
Base = make_base()
session = make_session(engine)
