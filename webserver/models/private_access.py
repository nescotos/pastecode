from webserver import rest_db
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship


class PrivateAccess(rest_db.Model):
    __tablename__ = 'private_access'
    _id = Column('_id', Integer(), primary_key=True)
    user_id = Column('user', Integer(), ForeignKey('users._id'))
    code_id = Column('code', Integer(), ForeignKey('codes._id'))

