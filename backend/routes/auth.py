from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId
from flask import current_app, request, jsonify, Blueprint
from flask_mail import Message
import jwt
from datetime import datetime, timedelta
from flask_cors import cross_origin

# Define the blueprint
auth_bp = Blueprint('auth', __name__)

class User:
    def __init__(self, username, email, password=None, password_hash=None, _id=None, verified=False, last_verification_email_sent=None, last_password_reset_email_sent=None):
        self.username = username
        self.email = email
        self.password_hash = password_hash
        self.verified = verified
        self.last_verification_email_sent = last_verification_email_sent
        self.last_password_reset_email_sent = last_password_reset_email_sent
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

    def to_dict(self):
        return {
            'id': str(self.id),
            'username': self.username,
            'email': self.email,
            'verified': self.verified
        }

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
                verified=user_data.get('verified', False),
                last_verification_email_sent=user_data.get('last_verification_email_sent'),
                last_password_reset_email_sent=user_data.get('last_password_reset_email_sent')
            )
        current_app.logger.debug('User not found by username: %s', username)
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
                verified=user_data.get('verified', False),
                last_verification_email_sent=user_data.get('last_verification_email_sent'),
                last_password_reset_email_sent=user_data.get('last_password_reset_email_sent')
            )
        current_app.logger.debug('User not found by email: %s', email)
        return None

    def save_to_db(self):
        user_data = {
            '_id': self.id,
            'username': self.username,
            'email': self.email,
            'password_hash': self.password_hash,
            'verified': self.verified,
            'last_verification_email_sent': self.last_verification_email_sent,
            'last_password_reset_email_sent': self.last_password_reset_email_sent
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
                verified=user_data.get('verified', False),
                last_verification_email_sent=user_data.get('last_verification_email_sent'),
                last_password_reset_email_sent=user_data.get('last_password_reset_email_sent')
            )
        current_app.logger.debug('User not found by ID: %s', user_id)
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

    @staticmethod
    def get_potential_friends(user_id):
        all_users = current_app.mongo.db.users.find({'_id': {'$ne': ObjectId(user_id)}})
        user = current_app.mongo.db.users.find_one({'_id': ObjectId(user_id)})
        friend_ids = [ObjectId(friend_id) for friend_id in user.get('friends', [])]

        potential_friends = []
        for u in all_users:
            if u['_id'] not in friend_ids:
                potential_friends.append(u)
        return potential_friends

@auth_bp.route('/login', methods=['POST', 'OPTIONS'])
@cross_origin()
def login():
    if request.method == 'OPTIONS':
        return _build_cors_prelight_response()
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    current_app.logger.debug('Login attempt for email: %s', email)
    user = User.get_user_by_email(email)
    if not user:
        current_app.logger.debug('Login failed: User not found')
        return jsonify({"message": "User not found"}), 404
    if not user.verified:
        current_app.logger.debug('Login failed: Email not confirmed')
        return jsonify({"message": "Email not confirmed"}), 401
    if user.check_password(password):
        token = jwt.encode({
            'user_id': str(user.id),
            'exp': datetime.utcnow() + timedelta(hours=1)
        }, current_app.config['SECRET_KEY'], algorithm='HS256')
        current_app.logger.debug('Login successful, token generated')
        return jsonify({"token": token})
    current_app.logger.debug('Login failed: Invalid credentials')
    return jsonify({"message": "Invalid credentials"}), 401

@auth_bp.route('/resend-verification', methods=['POST', 'OPTIONS'])
@cross_origin()
def resend_verification():
    if request.method == 'OPTIONS':
        return _build_cors_prelight_response()
    data = request.get_json()
    email = data.get('email')
    current_app.logger.debug('Resend verification email attempt for email: %s', email)
    user = User.get_user_by_email(email)
    if user and not user.verified:
        now = datetime.utcnow()
        if user.last_verification_email_sent and (now - user.last_verification_email_sent).total_seconds() < 3600:
            current_app.logger.debug('Resend verification failed: Email recently sent')
            return jsonify({"message": "Verification email recently sent. Please wait before requesting again."}), 429
        
        token = user.generate_verification_token()
        # Send the token via email to the user
        msg = Message(
            'Please verify your email',
            recipients=[email]
        )
        verification_url = f'http://localhost:8081/verify/{token}'
        msg.body = f'Please click the following link to verify your email: {verification_url}'
        try:
            current_app.mail.send(msg)
            user.last_verification_email_sent = now
            user.save_to_db()
            current_app.logger.debug('Verification email sent to %s', email)
            return jsonify({"message": "Verification email sent"})
        except Exception as e:
            current_app.logger.error('Failed to send verification email: %s', e)
            return jsonify({"message": "Failed to send verification email"}), 500
    current_app.logger.debug('Resend verification failed: User not found or already verified')
    return jsonify({"message": "User not found or already verified"}), 404


@auth_bp.route('/signup', methods=['POST', 'OPTIONS'])
@cross_origin()
def signup():
    if request.method == 'OPTIONS':
        return _build_cors_prelight_response()
    data = request.get_json()
    fullname = data.get('fullname')
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    current_app.logger.debug('Signup attempt for email: %s', email)

    if User.get_user_by_email(email):
        current_app.logger.debug('Signup failed: Email already registered')
        return jsonify({"error": "Email already registered"}), 400

    if User.get_user_by_username(username):
        current_app.logger.debug('Signup failed: Username already taken')
        return jsonify({"error": "Username already taken"}), 400

    new_user = User(
        username=username,
        email=email,
        password=password
    )
    new_user.save_to_db()
    current_app.logger.debug('New user saved to DB: %s', new_user.to_dict())

    verification_token = new_user.generate_verification_token()
    # Send verification email
    msg = Message(
        'Please verify your email',
        recipients=[email]
    )
    verification_url = f'http://localhost:8081/verify/{verification_token}'
    msg.body = f'Please click the following link to verify your email: {verification_url}'
    try:
        current_app.mail.send(msg)
        current_app.logger.debug('Verification email sent to %s', email)
    except Exception as e:
        current_app.logger.error('Failed to send verification email: %s', e)
        return jsonify({"message": "User created but failed to send verification email"}), 500

    return jsonify({"success": True, "message": "User created successfully. Please check your email to verify your account."}), 201



    current_app.logger.debug('Password reset request failed: User not found')
    return jsonify({"message": "User not found"}), 404

@auth_bp.route('/reset-password/<token>', methods=['POST', 'OPTIONS'])
@cross_origin()
def reset_password(token):
    if request.method == 'OPTIONS':
        return _build_cors_prelight_response()
    data = request.get_json()
    new_password = data.get('new_password')
    current_app.logger.debug('Resetting password with token: %s', token)
    email = User.verify_verification_token(token)
    if email:
        user = User.get_user_by_email(email)
        if user:
            user.set_password(new_password)
            user.save_to_db()
            current_app.logger.debug('Password reset successful for user: %s', email)
            return jsonify({"message": "Password reset successfully"}), 200
    current_app.logger.error('Password reset failed: Invalid or expired token')
    return jsonify({"message": "Invalid or expired token"}), 400
