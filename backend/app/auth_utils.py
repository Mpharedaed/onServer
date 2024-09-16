from flask import Blueprint, request, jsonify, current_app, url_for
from flask_jwt_extended import create_access_token
from model.user import User
from werkzeug.security import check_password_hash
from flask_mail import Message

auth_bp = Blueprint('auth', __name__)


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
