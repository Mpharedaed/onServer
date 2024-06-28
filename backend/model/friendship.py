from bson.objectid import ObjectId
from flask import current_app
from datetime import datetime

class Friendship:
    STATUS_PENDING = "pending"
    STATUS_ACCEPTED = "accepted"
    STATUS_BLOCKED = "blocked"

    def __init__(self, user1_id, user2_id, status=STATUS_PENDING, created_at=None, updated_at=None, _id=None):
        self.user1_id = user1_id
        self.user2_id = user2_id
        self.status = status
        self.created_at = created_at if created_at else datetime.utcnow()
        self.updated_at = updated_at
        if _id:
            self.id = _id
        else:
            self.id = ObjectId()

    def save_to_db(self):
        friendship_data = self.to_dict()
        current_app.mongo.db.friendships.replace_one({'_id': self.id}, friendship_data, upsert=True)

    @staticmethod
    def get_friendship_by_users(user1_id, user2_id):
        friendship_data = current_app.mongo.db.friendships.find_one({
            '$or': [
                {'user1_id': user1_id, 'user2_id': user2_id},
                {'user1_id': user2_id, 'user2_id': user1_id}
            ]
        })
        if friendship_data:
            return Friendship(**friendship_data)
        return None

    @staticmethod
    def get_friendships_by_user(user_id):
        friendships = current_app.mongo.db.friendships.find({
            '$or': [
                {'user1_id': user_id},
                {'user2_id': user_id}
            ]
        })
        return [Friendship(**friendship) for friendship in friendships]

    def accept_friendship(self):
        self.status = self.STATUS_ACCEPTED
        self.updated_at = datetime.utcnow()
        self.save_to_db()

    def block_friendship(self):
        self.status = self.STATUS_BLOCKED
        self.updated_at = datetime.utcnow()
        self.save_to_db()

    def delete_friendship(self):
        current_app.mongo.db.friendships.delete_one({'_id': self.id})

    def to_dict(self):
        return {
            '_id': self.id,
            'user1_id': self.user1_id,
            'user2_id': self.user2_id,
            'status': self.status,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
