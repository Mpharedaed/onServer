import os
from flask import Flask
from app.extensions import init_redis, limiter
from app.config import Config  # Import the config class
from routes.auth import auth_bp

app = Flask(__name__)

# Load configuration from Config class
app.config.from_object(Config)

# Initialize Redis and other components
init_redis(app)
limiter.init_app(app)

# Register Blueprints and other app components
# app.register_blueprint(auth_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000)))
