import redis
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

# Create a limiter instance
limiter = Limiter(key_func=get_remote_address)

# Redis client placeholder (to be initialized later)
redis_client = None

def init_redis(app):
    """Initialize the Redis client with the app configuration."""
    global redis_client
    redis_client = redis.Redis.from_url(app.config['REDIS_URL'])
