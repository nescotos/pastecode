from flask_restful import fields, marshal_with, reqparse, Resource
from webserver.models import User
from flask import jsonify

class UserAPI(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True)
        parser.add_argument('email', type=str, required=True)
        parser.add_argument('password', type=str, required=True)
        args = parser.parse_args()
        new_user = User(args)
        try:
            new_user.save()
            return jsonify(dict(status=True, message='Saved'))
        except:
            return jsonify(dict(status=False, message='Error'))


class UserAPIById(Resource):
    def get(self, user_id):
        user_to_get = User.query.filter_by(_id = user_id).first()
        if user_to_get is not None:
            return jsonify(dict(status=True, message='Enjoy the data', user=dict(name=user_to_get.name, email=user_to_get.email)))
        return jsonify(dict(status=False, message='User does not exist'))


