"""Stub file for respective models.

Delete the contents of this file and complete it with your solution.
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

ROOT = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(ROOT, '.env'))
URL = os.environ.get("URL")

Base = declarative_base()
engine = create_engine(URL)
Session = sessionmaker(bind=engine)
session = Session()