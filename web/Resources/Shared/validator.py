def validate_req_body(req_body, action):
   if action in ['add', 'multiply']:
      if 'x' not in req_body:
          return {"status_code": 400, "message": "x is required"}
      elif 'y' not in req_body:
          return {"status_code": 400, "message": "y is required"}
      else:
          return {"status_code": 200}
   elif action == 'divide':
        if 'x' not in req_body:
            return {"status_code": 400, "message": "x is required"}
        elif 'y' not in req_body:
            return {"status_code": 400, "message": "y is required"}
        elif int(req_body['y']) == 0:
            return { "status_code": 400, "message": "y is not suppose to be greater than 0"}
        else:
            return {"status_code": 200}