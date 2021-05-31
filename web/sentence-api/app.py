from flask import Flask
from flask_restful import Api

server = Flask(__name__, template_folder='templates')

# import env variables
from config import DEBUG, PORT

# import resources
from resources.home import Home
from resources.auth.register import Register
from resources.auth.verification import Verification
from resources.auth.reset_password import ResetPassword
from resources.auth.chang_password import ChangePass


def create_app():
    api = Api(server)

    # register the resources
    api.add_resource(Home, '/')
    api.add_resource(Register, '/auth/register')
    api.add_resource(Verification, '/auth/verification/<token>')
    api.add_resource(ResetPassword, '/auth/reset-password',  '/view/auth/reset-password')
    api.add_resource(ChangePass, '/view/auth/change-password/<reset_token>', '/auth/change-passoword/<reset_token>')

    return server

if __name__ == '__main__':
    create_app().run(debug=DEBUG, port=PORT)
