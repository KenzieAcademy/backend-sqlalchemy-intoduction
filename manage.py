import click

from rdbms.models.database import Base
from rdbms.models.database import Engine


@click.group()
def cli():
    pass


@cli.command()
def init():
    Base.metadata.create_all(Engine)


if __name__ == '__main__':
    cli()
