from webserver import rest_db
from sqlalchemy import Column, Integer, ForeignKey, Text, Boolean
from sqlalchemy.orm import relationship

class Code(rest_db.Model):
    __tablename__ = 'codes'
    _id = Column('_id', Integer(), primary_key=True)
    code = Column('code', Text())
    owner_id = Column('owner', Integer(), ForeignKey('users._id'))
    language_id = Column('language', Integer(), ForeignKey('languages._id'))
    isPublic = Column('isPublic', Boolean())
    language = relationship('Language', back_populates='codes')
    owner = relationship('User', back_populates='codes')

    
    def __init__(self, args):
        self.code = args['code']
        self.language_id = args['language']
        self.isPublic = args['isPublic']
        self.owner_id = args['owner']

    def save(self):
        rest_db.session.add(self)
        rest_db.session.commit()

    def update(self, args):
        try:
            rest_db.session.query(Class).filter_by(_id = self._id).update(args)
            rest_db.session.commit()
        except:
            rest_db.session.rollback()



