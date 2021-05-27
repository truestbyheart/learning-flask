from flask import Flask
from flask_restful import Api

# resources
import Resources.add as a
import Resources.multiply as m
import Resources.divide as d

app = Flask(__name__)

api = Api(app)

api.add_resource(a.Add, '/add')
api.add_resource(m.Multiply, '/multiply')
api.add_resource(d.Divide, '/division')

@app.route('/')
def home():
   return "Hello world"


if __name__ == "__main__":
    app.run(host='0.0.0.0')