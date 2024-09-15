import os
from flask import Flask
from flask_cors import CORS
from app.extensions import limiter  # Import limiter from extensions.py
from app.routes.auth import auth_bp  # Example: import auth blueprint

# Initialize Flask application
app = Flask(__name__)

# Initialize CORS
CORS(app, resources={r"/*": {"origins": "*"}})

# Initialize limiter with the app
limiter.init_app(app)

# Register blueprints
app.register_blueprint(auth_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000)))
