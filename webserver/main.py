from flask_restful import Api
from flask import request, jsonify
from webserver.models import User
from webserver.api import UserAPI, UserAPIById, CodeAPI, CodeAPIById
from webserver import app
from flask_jwt_extended import JWTManager, create_access_token, jwt_refresh_token_required, get_jwt_identity, create_access_token
from werkzeug.security import safe_str_cmp
from webserver.models.user import bcrypt

jwt = JWTManager(app)
rest_api = Api(app)

def authenticate(username, password):
    user = User.query.filter_by(name=username).first()
    if user and bcrypt.check_password_hash(user.password, password):
        return user._id
    return False
    
@app.route('/login', methods=['POST'])
def login():
    try:
        username = request.form['username']
        password = request.form['password']
        auth_result = authenticate(username, password)
        if auth_result is not False:
            return jsonify({'access_token': create_access_token(identity=auth_result)})
        return jsonify({'status': False, 'message': 'Username or password incorrect'}), 401
    except:
        return jsonify({'status': False, 'message': 'Missing fields'}), 400

@app.route('/refresh', methods=['POST'])
@jwt_refresh_token_required
def refresh():
    current_user = get_jwt_identity()
    return jsonify({'access_token': create_access_token(identity=current_user)})

rest_api.add_resource(UserAPI, '/user')
rest_api.add_resource(UserAPIById, '/user/<user_id>')
rest_api.add_resource(CodeAPI, '/code')
rest_api.add_resource(CodeAPIById, '/code/<code_id>')

