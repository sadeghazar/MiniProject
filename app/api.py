import os
from flask import Flask
from flask_jwt_extended.jwt_manager import JWTManager
from flask_restful import Api
from flask_migrate import Migrate
from app.db import db
from app.ma import ma
from app.resources.user import User
from app.resources.security import UserLogin, TokenRefresh

app = Flask(__name__)
api = Api(app)
POSTGRES = {
    'user': os.environ.get("DB_USER"),
    'password': os.environ.get("DB_PASS"),
    'db': os.environ.get("DB_NAME"),
    'host': os.environ.get("DB_HOST"),
}
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://{}:{}@{}/{}' \
    .format(POSTGRES['user'], POSTGRES['password'], POSTGRES['host'], POSTGRES['db'])
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['JWT_SECRET_KEY'] = 'rotyiutoiwuerotiupotijlkvmc'

migrate = Migrate(app, db)

jwt = JWTManager(app)


@app.before_first_request
def create_tables():
    db.create_all()
    db.session.commit()
    from app.models.user import UserModel
    if not UserModel.find_by_username("admin"):
        UserModel(username="admin", password="123", firstName="admin", lastName="admin"
                  , phoneNumber="123467890").save_to_db()


api.add_resource(User, '/user/<int:user_id>', "/user")
api.add_resource(UserLogin, '/login')
api.add_resource(TokenRefresh, '/token/refresh')

db.init_app(app)
ma.init_app(app)
if __name__ == "__main__":
    app.run(port=5000, debug=True, host="0.0.0.0")
