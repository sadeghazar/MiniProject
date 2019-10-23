from flask import Flask
from flask_restful import Api, Resource

from app.resources.user import User

app = Flask(__name__)
api = Api(app)


api.add_resource(User, '/user/<int:user_id>')


if __name__ == "__main__":
    app.run(port=5000, debug=True, host="0.0.0.0")
