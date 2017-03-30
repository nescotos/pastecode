from webserver import rest_db
from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

class Language(rest_db.Model):
    __tablename__ = 'languages'
    _id = Column('_id', Integer(), primary_key=True)
    name = Column('name', String(50))
    codes = relationship('Code', backref='languages', lazy='dynamic')
