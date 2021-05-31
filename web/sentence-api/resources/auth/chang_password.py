from flask import make_response, render_template, request
from flask_restful import Resource
from datetime import datetime
import jwt

# config 
from config import DOMAIN, JWT_SECRET

headers = {'Content-type': 'text/html'}

class ChangePass(Resource):
    def get(self, reset_token):
        print(reset_token)
        # Decode the Jwt token
        user = jwt.decode(reset_token, JWT_SECRET, algorithms=['HS256'])
        print(user)
        return make_response(render_template('change-password.html', year=datetime.today().year, username=user['username'], email=user['email']), 200, headers)
    
    def post(self):
        return 'OK'