import random

import click

from rdbms.models.database import Base, engine, session
from rdbms.models.users import Users
from rdbms.models.accounts import Accounts
from rdbms.models.addresses import Addresses
from rdbms.models.education import Education
from rdbms.models.employments import Employments
from rdbms.models.languages import Languages
from rdbms.models.profiles import Profiles
from rdbms.models.telephones import Telephones
from rdbms.models.vitals import Vitals


@click.group()
def cli():
    pass


@cli.command()
def init():
    Base.metadata.create_all(engine)
    Users._bootstrap()
    Accounts._bootstrap()
    Addresses._bootstrap()
    Education._bootstrap()
    Employments._bootstrap()
    Languages._bootstrap()
    Profiles._bootstrap()
    Telephones._bootstrap()
    Vitals._bootstrap()


if __name__ == '__main__':
    cli()
