from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import os


DATABASE_URL = os.getenv('DATABASE_URL')

Session = sessionmaker()
engine = create_engine(DATABASE_URL, echo=False)

Session.configure(bind=engine)
Base = declarative_base()
