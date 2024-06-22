from flask import Blueprint, request, jsonify, url_for, current_app
from flask_mail import Message
from flask_jwt_extended import jwt_required, get_jwt_identity
from .models import User, Post
import jwt
from flask_limiter.util import get_remote_address
from datetime import datetime, timedelta




# Initialize Flask Blueprint
auth_bp = Blueprint('auth', __name__)

# Import limiter from the main application file
from run import limiter

# Authentication routes
@auth_bp.route('/signup', methods=['POST'])
def signup():
    current_app.logger.info('Signup endpoint called.')
    data = request.get_json()
    current_app.logger.debug('Received data: %s', data)

    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    current_app.logger.info('Signup data received: username=%s, email=%s', username, email)

    if not username or not email or not password:
        current_app.logger.error('Missing username, email, or password.')
        return jsonify({'error': 'Username, email, and password are required'}), 400

    if User.get_user_by_email(email) or User.get_user_by_username(username):
        current_app.logger.error('User already exists.')
        return jsonify({'error': 'User already exists'}), 400

    new_user = User(username=username, email=email, password=password)
    current_app.logger.debug('New user created: %s', new_user)
    
    new_user.save_to_db()
    current_app.logger.info('New user saved to DB.')

    token = new_user.generate_verification_token()
    verification_url = url_for('auth.verify_email', token=token, _external=True)
    current_app.logger.info('Verification URL generated: %s', verification_url)

    send_verification_email(new_user.email, verification_url)

    return jsonify({"message": "User signed up successfully. Please check your email to verify your account."}), 201

def send_verification_email(to_email, verification_url):
    current_app.logger.info('Preparing to send verification email to %s', to_email)
    try:
        msg = Message('Verify Your Email Address', recipients=[to_email])
        msg.body = f'Please click the link to verify your email: {verification_url}'
        current_app.mail.send(msg)
        current_app.logger.info('Verification email sent to %s', to_email)
    except Exception as e:
        current_app.logger.error('Failed to send verification email: %s', str(e))

@auth_bp.route('/verify/<token>', methods=['GET'])
def verify_email(token):
    current_app.logger.info('Verify email endpoint called with token: %s', token)
    try:
        email = User.verify_verification_token(token)
        current_app.logger.info('Email decoded from token: %s', email)
        if email is None:
            raise ValueError('Invalid or expired token')
    except Exception as e:
        current_app.logger.error('Token verification failed: %s', str(e))
        return jsonify({'error': 'Invalid or expired token'}), 400

    try:
        user = User.get_user_by_email(email)
        if not user:
            current_app.logger.error('User not found for email: %s', email)
            return jsonify({'error': 'User not found'}), 404

        user.verified = True
        user.save_to_db()
        current_app.logger.info('User %s verified successfully.', user.email)
        return jsonify({'message': 'Email verified successfully!'}), 200
    except Exception as e:
        current_app.logger.error('Error during user verification: %s', str(e))
        return jsonify({'error': 'Internal server error'}), 500

@auth_bp.route('/login', methods=['POST'])
def login():
    current_app.logger.info('Login endpoint called.')
    data = request.get_json()
    current_app.logger.debug('Received data: %s', data)

    username = data.get('username')
    password = data.get('password')

    current_app.logger.info('Login attempt for user: %s', username)

    if not username or not password:
        current_app.logger.error('Username or password missing')
        return jsonify({'error': 'Username and password are required'}), 400

    user = User.get_user_by_username(username)
    current_app.logger.debug('User found: %s', user)

    if not user:
        current_app.logger.error('User %s not found.', username)
        return jsonify({'error': 'Invalid credentials'}), 401

    if not user.check_password(password):
        current_app.logger.error('Invalid password for user %s.', username)
        return jsonify({'error': 'Invalid credentials'}), 401

    if not user.verified:
        current_app.logger.error('User %s has not verified their email.', username)
        return jsonify({'error': 'Email not verified. Please check your email to verify your account.'}), 401

    token = jwt.encode({
        'user_id': str(user.id),
        'sub': str(user.id),  # Add the subject claim
        'exp': datetime.utcnow() + timedelta(hours=1)
    }, current_app.config['JWT_SECRET_KEY'], algorithm="HS256")

    current_app.logger.info('Login successful for user: %s', username)
    return jsonify({'token': token}), 200
