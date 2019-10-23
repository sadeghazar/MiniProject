from datetime import datetime

from flask_restful import Resource, reqparse

parser = reqparse.RequestParser()
parser.add_argument("first_name", type=str, required=True)
parser.add_argument("last_name", type=str, required=True)
parser.add_argument("phone_number", type=str, required=True)
parser.add_argument("birth_date", type=lambda x: datetime.strptime(x, '%Y-%m-%dT%H:%M:%S'), required=False)


class User(Resource):

    def get(self, user_id: int):
        return {"UserID": user_id}, 200

    def post(self):
        args = parser.parse_args(strict=True)
        first_name = args["first_name"]
        last_name = args["last_name"]
        phone_number = args["phone_number"]
        birth_date = args["birth_date"]
        return {"Message": "Created"}, 201

    def put(self, user_id: int):
        args = parser.parse_args(strict=True)
        first_name = args["first_name"]
        last_name = args["last_name"]
        phone_number = args["phone_number"]
        birth_date = args["birth_date"]
        return {"Message": "Updated"}, 204

    def delete(self, user_id: int):
        return {"Message": "Deleted"}, 202
