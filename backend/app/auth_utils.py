from flask import Blueprint, request, jsonify, current_app, url_for
from flask_jwt_extended import create_access_token
from model.user import User
from werkzeug.security import check_password_hash
from flask_mail import Message

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST', 'OPTIONS'])
def login():
    if request.method == 'OPTIONS':
        return jsonify({}), 200
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.get_user_by_username(username)
    if not user or not check_password_hash(user.password_hash, password):
        return jsonify({'error': 'Invalid credentials'}), 401

    if not user.verified:
        current_app.logger.error(f'User {username} has not verified their email.')
        return jsonify({'error': 'Email not verified. Please check your email to verify your account.'}), 401

    token = create_access_token(identity=str(user.id))
    return jsonify({'token': token}), 200

@auth_bp.route('/resend-verification', methods=['POST', 'OPTIONS'])
def resend_verification_email():
    if request.method == 'OPTIONS':
        return jsonify({}), 200
    data = request.get_json()
    email = data.get('email')

    user = User.get_user_by_email(email)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    if user.verified:
        return jsonify({'error': 'Email already verified'}), 400

    token = user.generate_verification_token()
    verification_url = url_for('auth.verify_email', token=token, _external=True)
    send_verification_email(user.email, verification_url)

    return jsonify({'message': 'Verification email resent'}), 200

def send_verification_email(to_email, verification_url):
    current_app.logger.info('Preparing to send verification email to %s', to_email)
    try:
        msg = Message('Verify Your Email Address', recipients=[to_email])
        msg.body = f'Please click the link to verify your email: {verification_url}'
        current_app.mail.send(msg)
        current_app.logger.info('Verification email sent to %s', to_email)
    except Exception as e:
        current_app.logger.error('Failed to send verification email: %s', str(e))
