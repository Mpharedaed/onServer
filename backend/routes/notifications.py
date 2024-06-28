# routes/notifications.py
from flask import Blueprint, request, jsonify, current_app
from flask_jwt_extended import jwt_required, get_jwt_identity
from model.notification import Notification  # Ensure correct import path

notification_bp = Blueprint('notifications', __name__)

@notification_bp.route('/notifications', methods=['GET'])
@jwt_required()
def get_notifications():
    user_id = get_jwt_identity()
    notifications = Notification.get_notifications_by_user(user_id)
    return jsonify([notification.to_dict() for notification in notifications]), 200
