from flask import Flask
from flask_restful import Api

# import resources
import resources.home as H
import resources.auth.register as R

app = Flask(__name__)

api = Api(app)

# register the resources
api.add_resource(H.Home, '/')
api.add_resource(R.Register, '/auth/register')

if __name__ == '__main__':
    app.run(debug=True)
