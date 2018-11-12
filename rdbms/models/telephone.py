from sqlalchemy import Column, Integer, ForeignKey, String

from rdbms.models.database import Base


class Telophone(Base):
    __tablename__ = 'telephones'

    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey('users.id'))
    telephone = Column(String)
