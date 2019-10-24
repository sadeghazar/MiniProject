from app.models.user import UserModel
from ma import ma


class UserSchema(ma.ModelSchema):
    class Meta:
        model = UserModel


user_schema = UserSchema()
users_schema = UserSchema(many=True)
