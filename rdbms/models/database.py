"""Stub file for respective models.

Delete the contents of this file and complete it with your solution.
"""
from .database_solution import (
    create_database_engine,
    create_database_connection,
    create_database_session,
    create_model_superclass,
    engine,
    session,
    Base
)
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///main.db')
# Session = sessionmaker()
# Session.configure(bind=engine)
