from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId
from flask import current_app

class User:
    def __init__(self, username, email, password=None, password_hash=None, _id=None):
        self.username = username
        self.email = email
        self.password_hash = password_hash
        if password:
            self.set_password(password)
        if _id:
            self.id = str(_id)
        else:
            self.id = str(ObjectId())

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @staticmethod
    def get_user_by_username(username):
        user_data = current_app.mongo.db.users.find_one({'username': username})
        if user_data:
            return User(**user_data)
        return None

    @staticmethod
    def get_user_by_email(email):
        user_data = current_app.mongo.db.users.find_one({'email': email})
        if user_data:
            return User(**user_data)
        return None

    def save_to_db(self):
        user_data = {
            "username": self.username,
            "email": self.email,
            "password_hash": self.password_hash,
            "_id": ObjectId(self.id)
        }
        current_app.mongo.db.users.insert_one(user_data)

    @staticmethod
    def find_by_id(user_id):
        user_data = current_app.mongo.db.users.find_one({'_id': ObjectId(user_id)})
        if user_data:
            return User(**user_data)
        return None
