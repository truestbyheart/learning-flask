from urllib import response
from flask import jsonify
from flask_restful import Resource
import jwt

# config
from config import JWT_SECRET

# db
from db import getDbInstance


class Verification(Resource):
    def get(self, token):
        # get db instance
        userCollection = getDbInstance()['users']

        # decode the jwt token
        obj = jwt.decode(token, JWT_SECRET, algorithms=['HS256'])

        # update the client verification state
        user = userCollection.find_one_and_update(
            {"email": obj['email']}, {"$set": {"is_verified": True}})

        # Generate access_token and refresh_token
        resp = {
            "access_token": jwt.encode({"username": user["username"], "full_name": user['full_name'], "email": user['email']}, JWT_SECRET, algorithm='HS256'),
            "refresh_token": jwt.encode({"user_id": user["email"]}, JWT_SECRET, algorithm='HS256')
        }
        return jsonify(resp)
