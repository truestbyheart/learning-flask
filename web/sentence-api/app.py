from flask import Flask
from flask_restful import Api

server = Flask(__name__)

# import env variables
from config import DEBUG, PORT

# import resources
from resources.home import Home
from resources.auth.register import Register
from resources.auth.verification import Verification

def create_app():
    api = Api(server)

    # register the resources
    api.add_resource(Home, '/')
    api.add_resource(Register, '/auth/register')
    api.add_resource(Verification, '/auth/verification/<token>')

    return server

if __name__ == '__main__':
    create_app().run(debug=DEBUG, port=PORT)
