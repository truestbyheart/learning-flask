
from flask import jsonify, request
from flask_restful import Resource
from bcrypt import hashpw, gensalt
from flask_mail import Message
import jwt
import os

from db import getDbInstance
from config import JWT_SECRET, DOMAIN, SENDER_EMAIL
from mail import getEmailInstance
from .register_schema import RegisterSchema


def check_duplicate_credentials(req_body, userCollection):
    # check if the email already exists
    email_check = userCollection.find_one(
        {"email": req_body['email']})

    # check if the username is taken
    username_check = userCollection.find_one(
        {"username": req_body['username']})

    if email_check is not None:
        return jsonify({"status": 409, "message": "email already exist"})
    elif username_check is not None:
        return jsonify({"status": 409, "message": "username is already taken"})

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
        hashedPassword = hashpw(req_body['password'].encode(
            'utf-8'), gensalt()).decode('utf-8')

        # create new user
        userCollection.insert_one({
            "full_name": req_body['full_name'],
            "username": req_body['username'],
            "email": req_body['email'],
            "password": hashedPassword,
            "is_verified": False,
            "sentence": {
                "limit": 10,
                "used": 0
            }
        })

        # generate verification token
        verification_jwt = jwt.encode(
            {"email": req_body['email']}, JWT_SECRET, algorithm='HS256')

        # send verification email to new client
        mailer = getEmailInstance()
          
        # create Message
        msg = Message('Please verify your email for SentenceHQ', sender=SENDER_EMAIL, recipients=[req_body['email']])
        msg.html = '<!DOCTYPE html><html lang="en"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"></head><body style="font-family: sans-serif;"><div style="display: block; margin: auto; max-width: 600px;"><p>Hi {username},</p><p>Please click the link below to activate your sentenceHQ account</p><p><a href="{verification}">Click Here</a></p></div></body></html>'.format(username=req_body['username'], verification=DOMAIN+'/auth/verification/'+verification_jwt)
        mailer.send(msg)

        return jsonify({"status": 201, "message": "Account created successfully, please verify you email"})
