import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()



class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String)

class Posts(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    title = Column(String)
    body = Column(String)

class Comments(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    body = Column(String)

class Tags(Base):
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    body = Column(String)

engine = create_engine('sqlite:///mydatabase.db', echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)


session = Session()

@click.group()
def cli():
    pass


@cli.command()
def init():
    Base.metadata.create_all(engine)

if __name__ == '__main__':
    cli()
