from functools import wraps
from flask import request, jsonify, current_app
import jwt
from bson.objectid import ObjectId
from .models import User

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('x-access-token')
        current_app.logger.debug('Token received: %s', token)
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401

        try:
            data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=["HS256"])
            current_app.logger.debug('Token data: %s', data)
            current_user = User.find_by_id(ObjectId(data['user_id']))
            current_app.logger.debug('Current user: %s', current_user)
            if not current_user:
                return jsonify({'message': 'User not found!'}), 401
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired!'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Token is invalid!'}), 401
        except Exception as e:
            return jsonify({'message': str(e)}), 401

        return f(current_user, *args, **kwargs)
    return decorated
