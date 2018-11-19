import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///:memory:", echo = True)
connection = engine.connect()

Session = sessionmaker(bind=connection)
session = Session()

Base = declarative_base()
