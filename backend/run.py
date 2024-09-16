import os
from flask import Flask
from app.extensions import init_redis, limiter
from app.config import Config  # Import the config class
from routes.auth import auth_bp
from app import create_app, mongo
from dotenv import load_dotenv
from flask_mail import Mail

# Load environment variables
load_dotenv()

# Initialize Flask-Mail
mail = Mail()  # This was missing in your original code

app = Flask(__name__)

# Load configuration from Config class
app.config.from_object(Config)

# Initialize Redis and other components
init_redis(app)
limiter.init_app(app)
mongo.init_app(app)  # Initialize MongoDB
mail.init_app(app)  # Initialize Flask-Mail with the app

# Register Blueprints and other app components
app.register_blueprint(auth_bp, url_prefix='/api/auth')

# app.register_blueprint(auth_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000)))
