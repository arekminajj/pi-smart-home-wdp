from flask import Flask
from flask_restful import Resource, Api, reqparse
from controller import status

app = Flask(__name__)
api = Api(app)

statusController = status("status.json")

parser = reqparse.RequestParser()
parser.add_argument('light_1')
parser.add_argument('temp_set')

class Home(Resource):
    def get(self):
        data = statusController.read()
        return data
    def post(self):
        args = parser.parse_args()
        statusController.write(args['light_1'], args['temp_set'])
        return args


api.add_resource(Home, "/")

if __name__ == "__main__":
    app.run(debug=True)
