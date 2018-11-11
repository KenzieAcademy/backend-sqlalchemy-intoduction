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
from mimesis import Person, Address, Datetime, Numbers, Business


@click.group()
def cli():
    pass


@cli.command()
def init():
    Base.metadata.create_all(engine)

    for mock_id in range(1, 51):
        person = Person('en')
        user = Users(
            username=person.username(),
            password=person.password(),
            email_address=person.email()
        )
        session.add(user)
        session.commit()
        for x in range(10):

            accounts = Accounts(
                user_id=mock_id,
                social_media_url=person.social_media_profile()
            )
            session.add(accounts)
            session.commit()

            address = Address('en')
            date = Datetime('en')
            numbers = Numbers('en')
            business = Business('en')

            addresses = Addresses(
                user_id=mock_id,
                street_address=address.address(),
                street_address_two=address.address(),
                city=address.city(),
                state=address.state(),
                postal_code=address.postal_code(),
                country=address.country(),
                start_date=date.date(start=1960, end=2012),
                end_date=date.date(start=2013, end=2019)
            )
            session.add(addresses)
            session.commit()

            education = Education(
                user_id=mock_id,
                school=person.university(),
                start_date=date.date(start=1980, end=2015),
                end_date=date.date(start=2016, end=2019),
                graduated=person.academic_degree(),
                gpa=numbers.rating(maximum=4.0)
            )
            session.add(education)
            session.commit()

            employments = Employments(
                user_id=mock_id,
                company=business.company(),
                occupation=person.occupation(),
                start_date=date.date(start=1980, end=2010),
                end_date=date.date(start=2011, end=2019)
            )
            session.add(employments)
            session.commit()

            languages = Languages(
                user_id=mock_id,
                language=person.language()
            )
            session.add(languages)
            session.commit()

            profiles = Profiles(
                user_id=mock_id,
                nationality=person.nationality()
            )
            session.add(profiles)
            session.commit()

            telephones = Telephones(
                user_id=mock_id,
                telephone_number=person.telephone(mask='', placeholder='#')
            )
            session.add(telephones)
            session.commit()

            vitals = Vitals(
                user_id=mock_id,
                height=person.height(),
                weight=person.weight()
            )
            session.add(vitals)
            session.commit()


if __name__ == '__main__':
    cli()
