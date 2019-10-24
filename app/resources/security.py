from flask_restful import Resource, reqparse
from app.models.user import UserModel
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required,
                                get_jwt_identity, get_raw_jwt)

parser = reqparse.RequestParser()
parser.add_argument("username", type=str, required=True, help="username required")
parser.add_argument("password", type=str, required=True, help="password required")


class UserLogin(Resource):
    def post(self):
        data = parser.parse_args()
        current_user = UserModel.login(data['username'], data['password'])
        if not current_user:
            return {'message': 'User {} doesn\'t exist'.format(data['username'])}

        access_token = create_access_token(identity=data['username'])
        refresh_token = create_refresh_token(identity=data['username'])

        return {
            'message': 'Logged in as {}'.format(current_user.username),
            'access_token': access_token,
            'refresh_token': refresh_token
        }


@jwt_refresh_token_required
class TokenRefresh(Resource):
    def post(self):
        current_user = get_jwt_identity()
        access_token = create_access_token(identity=current_user)
        return {'access_token': access_token}
