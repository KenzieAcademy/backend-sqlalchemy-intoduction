import click

from rdbms.models.database import Session
from rdbms.models.database import Base
from rdbms.models.database import engine
from rdbms.models.users import User
from rdbms.models.accounts import Account
from rdbms.models.addresses import Address
from rdbms.models.education import Education
from rdbms.models.employments import Employment
from rdbms.models.languages import Language
from rdbms.models.profiles import Profile
from rdbms.models.telephones import Telephone
from rdbms.models.vitals import Vitals


@click.group()
def cli():
    pass


@cli.command()
def init():
    Base.metadata.create_all(engine)
    User._bootstrap()
    sess = Session()
    for user in sess.query(User).all():
        Account._bootstrap(user)
        Address._bootstrap(user)
        Education._bootstrap(user)
        Employment._bootstrap(user)
        Language._bootstrap(user)
        Profile._bootstrap(user)
        Telephone._bootstrap(user)
        Vitals._bootstrap(user)
    sess.commit()


if __name__ == '__main__':
    cli()
