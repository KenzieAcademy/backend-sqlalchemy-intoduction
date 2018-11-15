"""Stub file for respective models.

Delete the contents of this file and complete it with your solution.
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///main.db')
Session = sessionmaker(bind=engine)
session = Session()