from flask_restful import Resource
from flask import make_response, render_template, request
from datetime import datetime
from flask_mail import Message
import jwt

# config
from config import JWT_SECRET, SENDER_EMAIL, DOMAIN

# utilities
from db import getDbInstance
from mail import getEmailInstance


class ResetPassword(Resource):
    def get(self):
        headers = {'Content-type': 'text/html'}
        return make_response(render_template('reset-password.html', year=datetime.today().year, user=None), 200, headers)

    def post(self):
        headers = {'Content-type': 'text/html'}
        # create db instance
        usersCollection = getDbInstance()['users']
        # get form input
        input = request.form.get('email')

        # find account on the database
        user = usersCollection.find_one({"$or": [
            {"email": input}, {"username": input}
        ]})

        if user is None:
            return make_response(render_template('reset-password.html', year=datetime.today().year, error=True), 200, headers)

        # Generate reset token

        reset_token = jwt.encode({"username": user['username'], "email": user['email'],
                                 "date_initiated": datetime.utcnow().isoformat().split('.')[0]}, JWT_SECRET, algorithm='HS256')

        # send email
        mailer = getEmailInstance()

        msg = Message('Reset Password | SentenceHQ',
                      sender=SENDER_EMAIL, recipients=[user['email']])
        msg.html = render_template(
            'reset-email.html', reset_link=DOMAIN + '/view/auth/change-password/' + reset_token, username=user['username'])

        mailer.send(msg)

        return make_response(render_template('reset-password.html', year=datetime.today().year, user=user), 200, headers)
