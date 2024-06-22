from flask import Blueprint, request, jsonify, current_app
from flask_jwt_extended import jwt_required, get_jwt_identity
from .models import Post

posts_bp = Blueprint('posts', __name__)

@posts_bp.route('/posts', methods=['POST'])
@jwt_required()
def create_post():
    current_app.logger.info('Create post endpoint called.')
    user_id = get_jwt_identity()
    data = request.get_json()
    current_app.logger.debug('Received data: %s', data)

    content = data.get('content')
    if not content:
        current_app.logger.error('Content is required')
        return jsonify({'error': 'Content is required'}), 400

    try:
        new_post = Post(
            user_id=user_id,
            content=content,
            likes=data.get('likes', 0),
            comments=data.get('comments', []),
            tags=data.get('tags', []),
            image_url=data.get('image_url'),
            is_pinned=data.get('is_pinned', False)
        )
        new_post.save_to_db()
        current_app.logger.info('New post created with id: %s', new_post.id)
        return jsonify({'message': 'Post created successfully', 'post_id': str(new_post.id)}), 201
    except Exception as e:
        current_app.logger.error('Error creating post: %s', str(e))
        return jsonify({'error': 'An error occurred creating the post'}), 500




@posts_bp.route('/user/posts', methods=['GET'])
@jwt_required()
def get_user_posts():
    user_id = get_jwt_identity()
    current_app.logger.info(f'Fetching posts for user {user_id}')
    try:
        posts = Post.get_posts_by_user(user_id)
        posts_data = [post.to_dict() for post in posts]
        return jsonify({'posts': posts_data}), 200
    except Exception as e:
        current_app.logger.error(f'Error fetching posts: {e}')
        return jsonify({'error': 'Failed to fetch posts'}), 500
