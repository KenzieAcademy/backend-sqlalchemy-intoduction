import click

from rdbms.models.database import Base
from rdbms.models.database import engine
from rdbms.models.posts import Posts
from rdbms.models.accounts import Accounts
from rdbms.models.addresses import Addresses
from rdbms.models.education import Education
from rdbms.models.users import Users
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
    Users()._bootstrap()
    Posts()._bootstrap()
    Accounts()._bootstrap()
    Addresses()._bootstrap()
    Education()._bootstrap()
    Languages()._bootstrap()
    Profiles()._bootstrap()
    Telephones()._bootstrap()
    Vitals()._bootstrap()



if __name__ == '__main__':
    cli()
