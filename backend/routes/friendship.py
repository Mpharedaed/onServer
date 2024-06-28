from flask import Blueprint, request, jsonify, current_app
from flask_jwt_extended import jwt_required, get_jwt_identity
from model.friendship import Friendship  # Corrected import path

friendship_bp = Blueprint('friendship', __name__)

@friendship_bp.route('/add', methods=['POST'])
@jwt_required()
def add_friend():
    current_app.logger.info('Add friend endpoint called.')
    data = request.get_json()
    current_app.logger.debug('Received data: %s', data)

    user1_id = get_jwt_identity()
    user2_id = data.get('user2_id')

    if not user2_id:
        return jsonify({'error': 'User ID required'}), 400

    existing_friendship = Friendship.get_friendship_by_users(user1_id, user2_id)
    if existing_friendship:
        return jsonify({'error': 'Friendship already exists'}), 400

    new_friendship = Friendship(user1_id=user1_id, user2_id=user2_id)
    new_friendship.save_to_db()

    return jsonify({'message': 'Friend request sent'}), 201
