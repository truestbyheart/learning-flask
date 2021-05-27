from sqlite3 import dbapi2
from flask import jsonify, request
from flask_restful import Resource
from marshmallow import Schema, fields

import resources.database.db as db


class RegisterSchema(Schema):
    """
    endpoint: /auth/register
    parameters:
        full_name: string,
        username: string,
        password: string,
        email: string
    """
    full_name = fields.Str(required=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True)
    email = fields.Email(required=True)


reg_validation_schema = RegisterSchema()


class Register(Resource):

    # def __init__(self, db):
    #     self.database = db

    def post(self):
        req_body = request.get_json()

        # validate the request body
        errors = reg_validation_schema.validate(req_body)
        if errors:
            return jsonify({"status": 400, "errors": errors})

        # check if the user exist
        print(db)
        userCollection = db['users']
        user = userCollection.find_one(
            {"email": req_body['email'], "username": req_body['username']})
        print(user)
        return jsonify({"status": 201, "message": "Account created successfully, please verify you email"})
