from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from model.user import User
from model.post import Post

user_bp = Blueprint('user', __name__)

@user_bp.route('/api/profile', methods=['GET'])
@jwt_required()
def get_profile():
    user_id = get_jwt_identity()
    user = User.find_by_id(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    # Fetch the user's posts
    posts = Post.get_posts_by_user(user_id)
    posts_dict = [post.to_dict() for post in posts]

    return jsonify({
        "username": user.username,
        "bio": user.bio,
        "avatar": user.avatar,
        "posts": posts_dict
    })
