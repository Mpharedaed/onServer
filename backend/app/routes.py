from flask import Blueprint, request, jsonify, current_app
from werkzeug.security import check_password_hash
import jwt
from datetime import datetime, timedelta
from .models import User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/api/signup', methods=['POST'])
def signup():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return jsonify({'error': 'Username, email, and password are required'}), 400

    if User.get_user_by_email(email) or User.get_user_by_username(username):
        return jsonify({'error': 'User already exists'}), 400

    new_user = User(username=username, email=email, password=password)
    new_user.save_to_db()

    return jsonify({"message": "User signed up successfully"}), 201

@auth_bp.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    current_app.logger.info(f'Attempting login for user: {username}')

    if not username or not password:
        current_app.logger.info(f'Username or password missing')
        return jsonify({'error': 'Username and password are required'}), 400

    user = User.get_user_by_username(username)

    if not user:
        current_app.logger.info(f'User {username} not found.')
        return jsonify({'error': 'Invalid credentials'}), 401

    if not user.check_password(password):
        current_app.logger.info(f'Invalid password for user {username}.')
        return jsonify({'error': 'Invalid credentials'}), 401

    token = jwt.encode({
        'user_id': str(user.id),
        'exp': datetime.utcnow() + timedelta(hours=1)
    }, current_app.config['SECRET_KEY'], algorithm="HS256")

    return jsonify({'token': token}), 200
