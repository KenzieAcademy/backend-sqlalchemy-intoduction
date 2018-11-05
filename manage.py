import click

from rdbms.models.database import Base
from rdbms.models.database import engine
from rdbms.models import *


@click.group()
def cli():
    pass


@cli.command()
def init():
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    cli()
