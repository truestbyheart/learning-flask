from flask import jsonify
from flask_restful import Resource

class Home(Resource):
    def get(self):
        return jsonify({ "status": 200, "message": "App is up and running" })
