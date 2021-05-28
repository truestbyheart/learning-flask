
from flask import jsonify, request
from flask_restful import Resource
from bcrypt import hashpw, gensalt
from flask_mail import Message

from db import getDbInstance
# from mail import getEmailInstance
from .register_schema import RegisterSchema


def check_duplicate_credentials(req_body, userCollection):
        # check if the email already exists
        email_check = userCollection.find_one(
            {"email": req_body['email']})

        # check if the username is taken
        username_check = userCollection.find_one(
            {"username": req_body['username']})

        if email_check is not None:
            return jsonify({"status": 409, "message":"email already exist"})
        elif username_check is not None:
            return jsonify({ "status": 409, "message": "username is already taken"})

        return None

class Register(Resource):
    def post(self):
        req_body = request.get_json()

        # validate the request body
        errors = RegisterSchema().validate(req_body)

        if errors:
            return jsonify({"status": 400, "errors": errors})

        # instantiate db
        userCollection = getDbInstance()['users']

        # check for duplicate entries i.e email and username
        has_duplicate = check_duplicate_credentials(req_body, userCollection)

        if has_duplicate is not None:
            return has_duplicate

        # hash password
        hashedPassword = hashpw(req_body['password'].encode('utf-8'), gensalt()).decode('utf-8')

        # create new user
        userCollection.insert_one({
            "full_name": req_body['full_name'],
            "username": req_body['username'],
            "email": req_body['email'],
            "password": hashedPassword,
            "is_verified": False
        })


        # send verification email to new client
        # mailer = getEmailInstance()

        # # create Message
        # msg = Message('Please verify your email for SentenceHQ', sender="margalight@0outlook.com", recipients=[req_body['email']])
        # msg.body = "hi ${req_body}, click the link below to verify your sentenHQ account"
        # mailer.send(msg)

        return jsonify({"status": 201, "message": "Account created successfully, please verify you email"})
