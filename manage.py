import click

from rdbms.models.database import Base
from rdbms.models.database import Engine
from rdbms.models.mimesis import Data_Gen


@click.group()
def cli():
    pass


@cli.command()
def init():
    Base.metadata.create_all(Engine)
    Data_Gen._bootstrap()


if __name__ == '__main__':
    cli()
