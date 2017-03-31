from webserver import rest_db, app
from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

class User(rest_db.Model):
    __tablename__ = 'users'
    _id = Column('_id', Integer(), primary_key=True)
    name = Column('name', String(50))
    email = Column(String(50))
    password = Column(String(250))
    codes = relationship('Code', backref='users')


    def __init__(self, args):
        self.name = args['name']
        self.email = args['email']
        self.password = bcrypt.generate_password_hash(args['password'])

    def save(self):
        rest_db.session.add(self)
        rest_db.session.commit()
