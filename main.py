from flask import Flask
from flask_restful import Resource, Api, reqparse
from controller import status
import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())
API_KEY = os.environ["API_KEY"]

app = Flask(__name__)
api = Api(app)
statusController = status("status.json")

parser = reqparse.RequestParser()
parser.add_argument('light_1')
parser.add_argument('temp_set')
parser.add_argument('API_KEY')


class Home(Resource):
    def get(self):
        data = statusController.read()
        return data
    def post(self):
        args = parser.parse_args()
        if args['API_KEY'] == API_KEY:
            statusController.write(args['light_1'], args['temp_set'])
            #usuwam API_KEY ze zwróconego JSONa dla bezpieczeństwa.
            del args["API_KEY"]
            return args
        return "API_KEY missing."
        
api.add_resource(Home, "/")

if __name__ == "__main__":
    app.run(debug=True)
