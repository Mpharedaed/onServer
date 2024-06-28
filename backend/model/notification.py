# model/notification.py
from bson.objectid import ObjectId
from flask import current_app
from datetime import datetime

class Notification:
    def __init__(self, user_id, message, read=False, created_at=None, _id=None):
        self.user_id = user_id
        self.message = message
        self.read = read
        self.created_at = created_at if created_at else datetime.utcnow()
        if _id:
            self.id = _id
        else:
            self.id = ObjectId()

    def save_to_db(self):
        notification_data = self.to_dict()
        current_app.mongo.db.notifications.replace_one({'_id': self.id}, notification_data, upsert=True)

    def mark_as_read(self):
        self.read = True
        self.save_to_db()

    @staticmethod
    def get_notifications_by_user(user_id):
        notifications = current_app.mongo.db.notifications.find({'user_id': user_id})
        return [Notification(**notification) for notification in notifications]

    def to_dict(self):
        return {
            '_id': self.id,
            'user_id': self.user_id,
            'message': self.message,
            'read': self.read,
            'created_at': self.created_at
        }
