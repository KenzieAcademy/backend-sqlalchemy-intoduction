from mimesis import Generic, Person, Internet, Address, Datetime, Business
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker

import random

from rdbms.models.accounts import Account
from rdbms.models.addresses import Addr
from rdbms.models.education import Education
from rdbms.models.database import Engine
from rdbms.models.employments import Employment
from rdbms.models.languages import Language
from rdbms.models.profiles import Profile
from rdbms.models.telephone import Telophone
from rdbms.models.users import User
from rdbms.models.vitals import Vital

g = Generic('pl')

Session = sessionmaker(bind=Engine)
session = Session()


class Data_Gen:

    def __init__(self, **kwargs):
        super(Data_Gen, self).__init__(**kwargs)

    @staticmethod
    def _bootstrap(count=1, locale='en'):
        person = Person('is')
        address = Address('en')
        datetime = Datetime('ru')
        business = Business()

        for _ in range(1, 51):
            # import ipdb; ipdb.set_trace()
            user = User(
                username=person.username(),
                email=person.email(),
                password=person.password()
            )
            session.add(user)
            try:
                session.commit()
                print('committed: user')
            except IntegrityError:
                session.rollback()
                print('commit failed')

        users = session.query(User).all()

        for user in users:
            for _ in range(1, 11):
                acct = Account(
                    user_id=user.id,
                    url=person.social_media_profile()
                )
                addrss = Addr(
                    user_id=user.id,
                    street_address=address.address(),
                    street_address_two=address.address(),
                    city=address.city(),
                    state=address.city(),
                    postal_code=address.postal_code(),
                    country=address.country(),
                    start_date=datetime.date(),
                    end_date=datetime.date()
                )
                edu = Education(
                    user_id=user.id,
                    school=person.name() + " high school",
                    start_date=datetime.date(),
                    end_date=datetime.date(),
                    graduated=True,
                    gpa=random.randint(1, 4)
                )
                employ = Employment(
                    user_id=user.id,
                    company=business.company(),
                    start_date=datetime.date(),
                    end_date=datetime.date(),
                    occupation=person.occupation()
                )
                lan = Language(
                    user_id=user.id,
                    language=person.language(),
                )
                prof = Profile(
                    user_id=user.id,
                    nationality=person.nationality(),
                )
                tel = Telophone(
                    user_id=user.id,
                    telephone=person.telephone(),
                )
                vit = Vital(
                    user_id=user.id,
                    weight=person.weight(),
                    height=person.height()
                )
                fields = [acct, addrss, employ, lan, prof, edu, tel, vit]
                session.add_all(fields)
                try:
                    session.commit()

                    print('committed')
                except IntegrityError:
                    print('commit failed')
                    session.rollback()
