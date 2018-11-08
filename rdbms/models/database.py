from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

import os

DATABASE_URL = os.environ['DATABASE_URL']
Base = declarative_base()
Engine = create_engine(
    DATABASE_URL)
