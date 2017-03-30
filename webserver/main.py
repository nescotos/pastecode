from flask_restful import Api
from flask import request, jsonify
from webserver.models import User
from webserver.api import UserAPI, UserAPIById
from webserver import app
from flask_jwt_extended import JWTManager, create_access_token
from werkzeug.security import safe_str_cmp
from webserver.models.user import bcrypt

jwt = JWTManager(app)
rest_api = Api(app)

def authenticate(username, password):
    user = User.query.filter_by(name=username).first()
    if user and bcrypt.check_password_hash(user.password, password):
        return True
    return False

def identity(payload):
    user_id = payload['identity']
    return User.query.filter_by(_id=user_id).first()

@app.route('/login', methods=['POST'])
def login():
    try:
        username = request.form['username']
        password = request.form['password']
        if authenticate(username, password):
            return jsonify({'access_token': create_access_token(identity=username)})
        return jsonify({'status': False, 'message': 'Username or password incorrect'}), 401
    except:
        return jsonify({'status': False, 'message': 'Missing fields'}), 400

rest_api.add_resource(UserAPI, '/user')
rest_api.add_resource(UserAPIById, '/user/<user_id>')

