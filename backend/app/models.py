from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId
from flask import current_app
import jwt
from datetime import datetime, timedelta

class User:
    def __init__(self, username, email, password=None, password_hash=None, _id=None, verified=False):
        self.username = username
        self.email = email
        self.password_hash = password_hash
        self.verified = verified
        if password:
            self.set_password(password)
        if _id:
            self.id = _id
        else:
            self.id = ObjectId()

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @staticmethod
    def get_user_by_username(username):
        current_app.logger.debug('Getting user by username: %s', username)
        user_data = current_app.mongo.db.users.find_one({'username': username})
        if user_data:
            current_app.logger.debug('User data found: %s', user_data)
            return User(
                username=user_data['username'],
                email=user_data['email'],
                password_hash=user_data['password_hash'],
                _id=user_data['_id'],
                verified=user_data.get('verified', False)
            )
        return None

    @staticmethod
    def get_user_by_email(email):
        current_app.logger.debug('Getting user by email: %s', email)
        user_data = current_app.mongo.db.users.find_one({'email': email})
        if user_data:
            current_app.logger.debug('User data found: %s', user_data)
            return User(
                username=user_data['username'],
                email=user_data['email'],
                password_hash=user_data['password_hash'],
                _id=user_data['_id'],
                verified=user_data.get('verified', False)
            )
        return None

    def save_to_db(self):
        user_data = {
            '_id': self.id,
            'username': self.username,
            'email': self.email,
            'password_hash': self.password_hash,
            'verified': self.verified
        }
        current_app.logger.debug('Saving user to DB: %s', user_data)
        current_app.mongo.db.users.replace_one({'_id': self.id}, user_data, upsert=True)

    @staticmethod
    def find_by_id(user_id):
        current_app.logger.debug('Finding user by ID: %s', user_id)
        user_data = current_app.mongo.db.users.find_one({'_id': ObjectId(user_id)})
        if user_data:
            current_app.logger.debug('User data found: %s', user_data)
            return User(
                username=user_data['username'],
                email=user_data['email'],
                password_hash=user_data['password_hash'],
                _id=user_data['_id'],
                verified=user_data.get('verified', False)
            )
        return None

    def generate_verification_token(self, expiration=3600):
        token = jwt.encode({
            'verify': self.email,
            'exp': datetime.utcnow() + timedelta(seconds=expiration)
        }, current_app.config['SECRET_KEY'], algorithm='HS256')
        current_app.logger.debug('Generated verification token: %s', token)
        return token

    @staticmethod
    def verify_verification_token(token):
        try:
            payload = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
            email = payload['verify']
            current_app.logger.debug('Token verified, email: %s', email)
            return email
        except jwt.ExpiredSignatureError:
            current_app.logger.error('Token verification error: Token expired')
            return None
        except jwt.InvalidTokenError:
            current_app.logger.error('Token verification error: Invalid token')
            return None
