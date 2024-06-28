from flask import Blueprint, request, jsonify, current_app
from flask_jwt_extended import jwt_required, get_jwt_identity
from model.friendship import AnonymousFriendship  # Updated import path

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

    existing_friendship = AnonymousFriendship.get_friendship_by_users(user1_id, user2_id)
    if existing_friendship:
        return jsonify({'error': 'Friendship already exists'}), 400

    new_friendship = AnonymousFriendship(user1_id=user1_id, user2_id=user2_id)
    new_friendship.save_to_db()

    return jsonify({'message': 'Friend request sent'}), 201

@friendship_bp.route('/accept', methods=['POST'])
@jwt_required()
def accept_friend():
    current_app.logger.info('Accept friend endpoint called.')
    data = request.get_json()
    current_app.logger.debug('Received data: %s', data)

    user1_id = get_jwt_identity()
    user2_id = data.get('user2_id')

    if not user2_id:
        return jsonify({'error': 'User ID required'}), 400

    friendship = AnonymousFriendship.get_friendship_by_users(user1_id, user2_id)
    if not friendship or friendship.status != AnonymousFriendship.STATUS_PENDING:
        return jsonify({'error': 'No pending friendship request found'}), 400

    friendship.accept_friendship()

    return jsonify({'message': 'Friend request accepted'}), 200

@friendship_bp.route('/block', methods=['POST'])
@jwt_required()
def block_friend():
    current_app.logger.info('Block friend endpoint called.')
    data = request.get_json()
    current_app.logger.debug('Received data: %s', data)

    user1_id = get_jwt_identity()
    user2_id = data.get('user2_id')

    if not user2_id:
        return jsonify({'error': 'User ID required'}), 400

    friendship = AnonymousFriendship.get_friendship_by_users(user1_id, user2_id)
    if not friendship:
        return jsonify({'error': 'No friendship found'}), 400

    friendship.block_friendship()

    return jsonify({'message': 'Friendship blocked'}), 200

@friendship_bp.route('/delete', methods=['POST'])
@jwt_required()
def delete_friend():
    current_app.logger.info('Delete friend endpoint called.')
    data = request.get_json()
    current_app.logger.debug('Received data: %s', data)

    user1_id = get_jwt_identity()
    user2_id = data.get('user2_id')

    if not user2_id:
        return jsonify({'error': 'User ID required'}), 400

    friendship = AnonymousFriendship.get_friendship_by_users(user1_id, user2_id)
    if not friendship:
        return jsonify({'error': 'No friendship found'}), 400

    friendship.delete_friendship()

    return jsonify({'message': 'Friendship deleted'}), 200

@friendship_bp.route('/interaction', methods=['POST'])
@jwt_required()
def add_interaction():
    current_app.logger.info('Add interaction endpoint called.')
    data = request.get_json()
    current_app.logger.debug('Received data: %s', data)

    user1_id = get_jwt_identity()
    user2_id = data.get('user2_id')

    if not user2_id:
        return jsonify({'error': 'User ID required'}), 400

    friendship = AnonymousFriendship.get_friendship_by_users(user1_id, user2_id)
    if not friendship:
        return jsonify({'error': 'No friendship found'}), 400

    friendship.add_interaction()

    return jsonify({'message': 'Interaction added'}), 200

@friendship_bp.route('/complete_quest', methods=['POST'])
@jwt_required()
def complete_quest():
    current_app.logger.info('Complete quest endpoint called.')
    data = request.get_json()
    current_app.logger.debug('Received data: %s', data)

    user1_id = get_jwt_identity()
    user2_id = data.get('user2_id')

    if not user2_id:
        return jsonify({'error': 'User ID required'}), 400

    friendship = AnonymousFriendship.get_friendship_by_users(user1_id, user2_id)
    if not friendship:
        return jsonify({'error': 'No friendship found'}), 400

    friendship.complete_quest()

    return jsonify({'message': 'Quest completed'}), 200

@friendship_bp.route('/reveal', methods=['POST'])
@jwt_required()
def reveal_identity():
    current_app.logger.info('Reveal identity endpoint called.')
    data = request.get_json()
    current_app.logger.debug('Received data: %s', data)

    user1_id = get_jwt_identity()
    user2_id = data.get('user2_id')

    if not user2_id:
        return jsonify({'error': 'User ID required'}), 400

    friendship = AnonymousFriendship.get_friendship_by_users(user1_id, user2_id)
    if not friendship:
        return jsonify({'error': 'No friendship found'}), 400

    friendship.reveal_identity()

    return jsonify({'message': 'Identity revealed'}), 200
