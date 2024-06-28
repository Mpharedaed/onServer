from bson.objectid import ObjectId
from flask import current_app
from datetime import datetime

class AnonymousFriendship:
    STATUS_PENDING = "pending"
    STATUS_ACCEPTED = "accepted"
    STATUS_BLOCKED = "blocked"

    def __init__(self, user1_id, user2_id, status=STATUS_PENDING, created_at=None, updated_at=None, level=1, interactions=0, quests_completed=0, virtual_currency=0, badges=None, revealed=False, _id=None):
        self.user1_id = user1_id
        self.user2_id = user2_id
        self.status = status
        self.created_at = created_at if created_at else datetime.utcnow()
        self.updated_at = updated_at
        self.level = level
        self.interactions = interactions
        self.quests_completed = quests_completed
        self.virtual_currency = virtual_currency
        self.badges = badges if badges is not None else []
        self.revealed = revealed
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
            return AnonymousFriendship(**friendship_data)
        return None

    @staticmethod
    def get_friendships_by_user(user_id):
        friendships = current_app.mongo.db.friendships.find({
            '$or': [
                {'user1_id': user_id},
                {'user2_id': user_id}
            ]
        })
        return [AnonymousFriendship(**friendship) for friendship in friendships]

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

    def add_interaction(self):
        self.interactions += 1
        self.virtual_currency += 10  # Earn virtual currency for each interaction
        self.check_level_up()
        self.updated_at = datetime.utcnow()
        self.save_to_db()

    def complete_quest(self):
        self.quests_completed += 1
        self.virtual_currency += 50  # Earn more currency for completing quests
        self.check_level_up()
        self.updated_at = datetime.utcnow()
        self.save_to_db()

    def check_level_up(self):
        # Example logic for leveling up
        if self.interactions >= 10 and self.level == 1:
            self.level = 2
            self.badges.append("Level 2 Achiever")
        elif self.interactions >= 50 and self.level == 2:
            self.level = 3
            self.badges.append("Level 3 Master")
        # Add more levels as needed

    def reveal_identity(self):
        self.revealed = True
        self.updated_at = datetime.utcnow()
        self.save_to_db()

    def to_dict(self):
        return {
            '_id': self.id,
            'user1_id': self.user1_id,
            'user2_id': self.user2_id,
            'status': self.status,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'level': self.level,
            'interactions': self.interactions,
            'quests_completed': self.quests_completed,
            'virtual_currency': self.virtual_currency,
            'badges': self.badges,
            'revealed': self.revealed
        }
