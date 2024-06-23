
from flask import Blueprint, request, jsonify, current_app
from .models import User
import jwt
from bson.objectid import ObjectId
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.find_by_username(username)
    if not user or not check_password_hash(user.password, password):
        return jsonify({'error': 'Invalid credentials'}), 401

    if not user.verified:
        return jsonify({'error': 'Email not verified. Please check your email to verify your account.'}), 401

    token = create_access_token(identity=str(user.id))
    return jsonify({'token': token}), 200

@auth_bp.route('/resend-verification', methods=['POST'])
def resend_verification_email():
    data = request.get_json()
    email = data.get('email')

    user = User.find_by_email(email)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    if user.verified:
        return jsonify({'error': 'Email already verified'}), 400

    # Here you should implement your logic to resend the verification email
    return jsonify({'message': 'Verification email resent'}), 200
