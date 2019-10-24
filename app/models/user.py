from app.db import db
from passlib.hash import bcrypt


class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(1024), nullable=False)
    firstName = db.Column(db.String(80), nullable=False)
    lastName = db.Column(db.String(80), nullable=False)
    phoneNumber = db.Column(db.String(80), nullable=False)
    birthDate = db.Column(db.DateTime, nullable=True)

    def __init__(self, username: str, password: str, firstName: str,
                 lastName: str, phoneNumber: str, birthDate):
        self.username = username
        self.password = bcrypt.hash(password)
        self.firstName = firstName
        self.lastName = lastName
        self.phoneNumber = phoneNumber
        self.birthDate = birthDate

    @classmethod
    def find_by_username(cls, username: str) -> "UserModel":
        return cls.query.filter_by(username=username).first()

    @classmethod
    def login(cls, username, password) -> "UserModel":
        return cls.query.filter_by(username=username, password=bcrypt.hash(password)).first()

    @classmethod
    def find_by_id(cls, _id: int) -> "UserModel":
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def get_all_users(cls) -> list:
        return cls.query.all()

    def update(self) -> None:
        db.session.commit()

    def save_to_db(self) -> "UserModel":
        db.session.add(self)
        db.session.commit()
        return self

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
