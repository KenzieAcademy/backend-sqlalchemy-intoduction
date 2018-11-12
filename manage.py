"""SQLAlchemy management commands."""
import click

from rdbms.models.database import Base
from rdbms.models.database import engine


@click.group()
def cli():
    pass


@cli.command()
def init():
    """Initialize database."""
    Base.metadata.create_all(engine)


@cli.command()
def seed():
    """Seed database."""
    import os
    os.system("python {}".format('./rdbms/seeds_solution.py'))


@cli.command()
def wipe():
    """Remove existing database, initialize and seed new database."""
    import os
    os.system("rm {}".format(os.getenv('DATABASE_URI').split('/')[-1]))
    os.system("python manage.py init")
    os.system("python manage.py seed")


if __name__ == '__main__':
    cli()
