import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv


db_url = os.getenv('DB_URL', 'sqlite:///knob.db')
Base = declarative_base()
engine = create_engine(db_url, echo=False)
Session = sessionmaker(bind=engine)
session = Session() 
