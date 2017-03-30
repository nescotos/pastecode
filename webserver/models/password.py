from webserver import rest_db
from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

class Password(rest_db.Model):
    __tablename__ = 'passwords_private_access'
    _id = Column('_id', Integer(), primary_key=True)
    private_acess_id = Column('private_access', String(250), ForeignKey('private_access._id'))
    password = Column('password', String(250))
