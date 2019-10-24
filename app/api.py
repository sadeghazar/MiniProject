import os

from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate
from app.db import db
from app.resources.user import User
from app.ma import ma

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
migrate = Migrate(app, db)


@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(User, '/user/<int:user_id>', "/user")

db.init_app(app)
ma.init_app(app)
if __name__ == "__main__":
    app.run(port=5000, debug=True, host="0.0.0.0")
