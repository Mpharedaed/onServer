from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_cors import CORS
from app.routes import auth_bp

# Initialize Flask application
app = Flask(__name__)

# Initialize CORS
CORS(app, resources={r"/*": {"origins": "*"}})  # Allow all origins for simplicity

# Initialize Limiter
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["200 per day", "50 per hour"]
)

# Register Blueprints
app.register_blueprint(auth_bp)

# Other configurations...

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)
