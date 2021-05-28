import os
import re

from flask import Flask
from flask_restful import Api

# import resources
from resources.home import Home
from resources.auth.register import Register

def create_app():
    server = Flask(__name__)
    api = Api(server)

    # register the resources
    api.add_resource(Home, '/')
    api.add_resource(Register, '/auth/register')

    return server

if __name__ == '__main__':
    create_app().run(debug=True)
