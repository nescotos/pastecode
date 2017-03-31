from flask_restful import fields, marshal_with, reqparse, Resource
from webserver.models import Code, User
from flask import jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required
from sqlalchemy import and_

class CodeAPI(Resource):
    @jwt_required
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('code', type=str, required=True)
        parser.add_argument('language', type=int, required=True)
        parser.add_argument('isPublic', type=bool, required=True)
        args = parser.parse_args()
        args['owner'] = get_jwt_identity() 
        new_code = Code(args)
        try:
            new_code.save()
            return jsonify(dict(status=True, message='Saved'))
        except:
            return jsonify(dict(status=False, message='Error'))

class CodeAPIById(Resource):
    @jwt_required
    def put(self, code_id):
        parser = reqparse.RequestParser()
        parser.add_argument('code', type=str)
        parser.add_argument('language', type=int)
        parser.add_argument('isPublic', type=bool)
        args = parser.parse_args()
        argsToUpdate = {}
        for k,v in args.iteritems():
            if v is not None:
                argsToUpdate[k] = v
        code_to_update = Code.query.filter_by(_id=code_id).first()
        if code_to_update is not None and code_to_update.owner_id is get_jwt_identity():
            try:
                code_to_update.update(argsToUpdate)   
                return jsonify(dict(status=True, message='Updated'))
            except ValueError:
                return jsonify(dict(status=False, message='Something Went Wrong', error=ValueError.message))
        return jsonify(dict(status=False, message='Code does not exist or does not belong to you'))

    @jwt_required
    def delete(self, code_id):
        code_to_delete = Code.query.filter_by(_id=code_id).first()
        if code_to_delete is not None and code_to_delete.owner_id is get_jwt_identity():
            try:
                code_to_delete.delete()
                return jsonify(dict(status=True, message='Code Deleted'))
            except:
                return jsonify(dict(status=False, message='Something Went Wrong'))
        return jsonify(dict(status=False, message='Code does not exist o does not belong to you'))


    def get(self, code_id):
        code_all = Code.query.filter_by(_id = code_id).first()
        if code_all is not None:
            return jsonify(dict(status=True, code=dict(
                id = code_all._id,
                code = code_all.code,
                language = code_all.language.name,
                user = dict(
                    id = code_all.owner._id,
                    name = code_all.owner.name
                )
            )))
        return jsonify(dict(status=False, message='Code does not exist'))


