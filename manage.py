"""SQLAlchemy management commands."""
import click
from rdbms.models.database import Base
from rdbms.models.database import engine
from rdbms.models.users import Users
from rdbms.models.accounts import Accounts
from rdbms.models.addresses import Addresses
from rdbms.models.education import Education
from rdbms.models.employment import Employments
from rdbms.models.languages import Languages
from rdbms.models.profiles import Profiles
from rdbms.models.phone_numbers import Telephones
from rdbms.models.vitals import Vitals


@click.group()
def cli():
    pass


@cli.command()
def init():
    """Initialize database."""
    Base.metadata.create_all(engine)
    Users._bootstrap()
    Accounts._bootstrap()
    Addresses._bootstrap()
    Education._bootstrap()
    Employments._bootstrap()
    Languages._bootstrap()
    Profiles._bootstrap()
    Telephones._bootstrap()


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
