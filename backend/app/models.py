# models.py
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
            'user_id': str(self.id),
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
class Post:
    def __init__(self, user_id, content, likes=0, comments=None, created_at=None, updated_at=None, tags=None, image_url=None, is_pinned=False, _id=None):
        self.user_id = user_id
        self.content = content
        self.likes = likes
        self.comments = comments if comments is not None else []
        self.created_at = created_at if created_at else datetime.utcnow()
        self.updated_at = updated_at
        self.tags = tags if tags is not None else []
        self.image_url = image_url
        self.is_pinned = is_pinned
        if _id:
            self.id = _id
        else:
            self.id = ObjectId()

    def save_to_db(self):
        try:
            post_data = {
                '_id': self.id,
                'user_id': self.user_id,
                'content': self.content,
                'likes': self.likes,
                'comments': self.comments,
                'created_at': self.created_at,
                'updated_at': self.updated_at,
                'tags': self.tags,
                'image_url': self.image_url,
                'is_pinned': self.is_pinned
            }
            current_app.mongo.db.posts.replace_one({'_id': self.id}, post_data, upsert=True)
            return True
        except Exception as e:
            current_app.logger.error(f'Error saving post to database: {e}')
            return False

    @staticmethod
    def get_post_by_id(post_id):
        post_data = current_app.mongo.db.posts.find_one({'_id': ObjectId(post_id)})
        if post_data:
            return Post(**post_data)
        return None

    @staticmethod
    def get_all_posts():
        posts = current_app.mongo.db.posts.find()
        return [Post(**post) for post in posts]

    @staticmethod
    def get_posts_by_user(user_id):
        posts = current_app.mongo.db.posts.find({'user_id': user_id})
        return [Post(**post) for post in posts]

    def add_comment(self, comment):
        self.comments.append(comment)
        self.updated_at = datetime.utcnow()
        self.save_to_db()

    def like_post(self):
        self.likes += 1
        self.updated_at = datetime.utcnow()
        self.save_to_db()

    def delete_post(self):
        current_app.mongo.db.posts.delete_one({'_id': self.id})

    def edit_post(self, content):
        self.content = content
        self.updated_at = datetime.utcnow()
        self.save_to_db()

    @staticmethod
    def search_posts(keyword):
        posts = current_app.mongo.db.posts.find({'content': {'$regex': keyword, '$options': 'i'}})
        return [Post(**post) for post in posts]

    def pin_post(self):
        self.is_pinned = True
        self.updated_at = datetime.utcnow()
        self.save_to_db()

    def unpin_post(self):
        self.is_pinned = False
        self.updated_at = datetime.utcnow()
        self.save_to_db()

    def to_dict(self):
        return {
            'id': str(self.id),
            'user_id': self.user_id,
            'content': self.content,
            'likes': self.likes,
            'comments': self.comments,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
            'tags': self.tags,
            'image_url': self.image_url,
            'is_pinned': self.is_pinned
        }