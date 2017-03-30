from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pastecode.db'
app.secret_key = '78Ii4UhQABvUovh5NJaS8J'
rest_db = SQLAlchemy(app)

import webserver.main
