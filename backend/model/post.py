from bson.objectid import ObjectId
from flask import current_app
from datetime import datetime

class Post:
    def __init__(self, user_id, content, likes=0, comments=None, created_at=None, updated_at=None, tags=None, image_url=None, is_pinned=False, is_anonymous=False, _id=None):
        self.user_id = user_id
        self.content = content
        self.likes = likes
        self.comments = comments if comments is not None else []
        self.created_at = created_at if created_at else datetime.utcnow()
        self.updated_at = updated_at
        self.tags = tags if tags is not None else []
        self.image_url = image_url
        self.is_pinned = is_pinned
        self.is_anonymous = is_anonymous  # Add this line
        if _id:
            self.id = _id
        else:
            self.id = ObjectId()

    def save_to_db(self):
        try:
            post_data = {
                '_id': self.id,
                'user_id': self.user_id,
                'content': self.content,
                'likes': self.likes,
                'comments': self.comments,
                'created_at': self.created_at,
                'updated_at': self.updated_at,
                'tags': self.tags,
                'image_url': self.image_url,
                'is_pinned': self.is_pinned,
                'is_anonymous': self.is_anonymous  # Add this line
            }
            current_app.mongo.db.posts.replace_one({'_id': self.id}, post_data, upsert=True)
            return True
        except Exception as e:
            current_app.logger.error(f'Error saving post to database: {e}')
            return False

    @staticmethod
    def get_post_by_id(post_id):
        post_data = current_app.mongo.db.posts.find_one({'_id': ObjectId(post_id)})
        if post_data:
            return Post(**post_data)
        return None

    @staticmethod
    def get_all_posts():
        posts = current_app.mongo.db.posts.find()
        return [Post(**post) for post in posts]

    @staticmethod
    def get_posts_by_user(user_id):
        posts = current_app.mongo.db.posts.find({'user_id': user_id})
        return [Post(**post) for post in posts]

    def add_comment(self, comment):
        self.comments.append(comment)
        self.updated_at = datetime.utcnow()
        self.save_to_db()

    def like_post(self):
        self.likes += 1
        self.updated_at = datetime.utcnow()
        self.save_to_db()

    def delete_post(self):
        current_app.mongo.db.posts.delete_one({'_id': self.id})

    def edit_post(self, content):
        self.content = content
        self.updated_at = datetime.utcnow()
        self.save_to_db()

    @staticmethod
    def search_posts(keyword):
        posts = current_app.mongo.db.posts.find({'content': {'$regex': keyword, '$options': 'i'}})
        return [Post(**post) for post in posts]

    def pin_post(self):
        self.is_pinned = True
        self.updated_at = datetime.utcnow()
        self.save_to_db()

    def unpin_post(self):
        self.is_pinned = False
        self.updated_at = datetime.utcnow()
        self.save_to_db()

    def to_dict(self):
        return {
            'id': str(self.id),
            'user_id': self.user_id,
            'content': self.content,
            'likes': self.likes,
            'comments': self.comments,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
            'tags': self.tags,
            'image_url': self.image_url,
            'is_pinned': self.is_pinned,
            'is_anonymous': self.is_anonymous  # Add this line
        }
