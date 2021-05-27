from flask import request
from flask_restful import Resource

import Resources.Shared.validator as validator

"""
all division related operation will be performed here
"""

class Divide(Resource):

    def post(self):
        req_body = request.get_json()
        # validate the request body
        check = validator.validate_req_body(req_body, 'divide')

        # if there is validation error respond
        if check['status_code'] != 200:
            return check

        result = int(req_body['x']) / int(req_body['y'])
        return {"status_code": 200,  "result": result}
