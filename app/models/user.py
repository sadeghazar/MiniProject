from app.db import db
from passlib.hash import pbkdf2_sha256 as sha256


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
                 lastName: str, phoneNumber: str, birthDate = None):
        self.username = username
        self.password = self.generate_hash(password)
        self.firstName = firstName
        self.lastName = lastName
        self.phoneNumber = phoneNumber
        self.birthDate = birthDate

    @classmethod
    def find_by_username(cls, username: str) -> "UserModel":
        return cls.query.filter_by(username=username).first()

    @classmethod
    def login(cls, username: str, password: str) -> "UserModel":
        user = cls.query.filter_by(username=username).first()
        if user:
            if cls.verify_hash(password, user.password):
                return user
        return None

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

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password, hash):
        return sha256.verify(password, hash)
