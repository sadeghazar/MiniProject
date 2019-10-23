from datetime import datetime

from flask_restful import Resource, reqparse

parser = reqparse.RequestParser()
parser.add_argument("FirstName", type=str, required=True)
parser.add_argument("LastName", type=str, required=True)
parser.add_argument("PhoneNumber", type=str, required=True)
parser.add_argument("BirthDate", type=datetime, required=False)


class User(Resource):

    def get(self, user_id: int):
        return {"UserID": user_id}, 200

    def post(self):
        args = parser.parse_args(strict=True)
        first_name = args["FirstName"]
        last_name = args["FirstName"]
        phone_number = args["FirstName"]
        birth_date = args["BirthDate"]
        return {"Message": "Created"}, 201
