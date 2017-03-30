from webserver import rest_db
from sqlalchemy import Column, Integer, ForeignKey, Text, Boolean
from sqlalchemy.orm import relationship

class Code(rest_db.Model):
    __tablename__ = 'codes'
    _id = Column('_id', Integer(), primary_key=True)
    code = Column('name', Text())
    owner_id = Column('owner', Integer(), ForeignKey('users._id'))
    language_id = Column('language', Integer(), ForeignKey('languages._id'))
    is_public = Column('isPublic', Boolean())
    language = relationship('Language', back_populates='codes')

