from datetime import datetime

from flask_jwt_extended.view_decorators import jwt_required
from flask_restful import Resource, reqparse
from flask import request
from app.models.user import UserModel
from schemas.user import UserSchema

parser = reqparse.RequestParser()
parser.add_argument("username", type=str, required=True, help="username required")
parser.add_argument("password", type=str, required=True, help="password required")
parser.add_argument("first_name", type=str, required=True, help="first_name required")
parser.add_argument("last_name", type=str, required=True, help="last_name required")
parser.add_argument("phone_number", type=str, required=True, help="phone_number required")
parser.add_argument("birth_date", type=lambda x: datetime.strptime(x, '%Y-%m-%dT%H:%M:%S')
                    , required=False, help="birth_date is invalid correct format is"
                                           "'%Y-%m-%dT%H:%M:%S")

user_schema = UserSchema()


class User(Resource):
    @jwt_required
    def get(self, user_id: int):
        user = UserModel.find_by_id(user_id)
        if user:
            return user_schema.dump(user), 200

        return None, 404

    def post(self):
        args = parser.parse_args(strict=True)
        username = args["username"]
        password = args["password"]
        first_name = args["first_name"]
        last_name = args["last_name"]
        phone_number = args["phone_number"]
        birth_date = args["birth_date"]
        user = UserModel.find_by_username(username)
        if user:
            return {"Message:": "this username is already taken"}, 409

        ret = UserModel(username=username, password=password, firstName=first_name,
                        lastName=last_name, phoneNumber=phone_number,
                        birthDate=birth_date).save_to_db()

        return {"Message": "Created", "user_id": ret.id}, 201

    def put(self, user_id: int):
        try:
            first_name = request.form["first_name"]
            last_name = request.form["last_name"]
            phone_number = request.form["phone_number"]
            birth_date = request.form["birth_date"]
            print(birth_date)
            user = UserModel.find_by_id(user_id)
            if user:
                user.firstName = first_name or user.firstName
                user.lastName = last_name or user.lastName
                user.phoneNumber = phone_number or user.phoneNumber
                user.birthDate = birth_date or user.birthDate
                user.firstName = first_name or user.firstName
                user.update()
                return {"Message": "Updated"}, 204
        except Exception as ex:
            print(ex)

    def delete(self, user_id: int):
        user = UserModel.find_by_id(user_id)
        if user:
            user.delete_from_db()
            return {"Message": "Deleted"}, 202
        return {"user not found"}, 404
