# app/__init__.py
from flask import Flask
from flask_cors import CORS
from flask_pymongo import PyMongo
from flask_mail import Mail
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def create_app():
    app = Flask(__name__)

    # Load configurations from environment variables
    app.config['MONGO_URI'] = os.getenv('MONGO_URI')
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
    app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
    app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER')
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
    app.config['JWT_TOKEN_LOCATION'] = ['headers']
    app.config['UPLOAD_FOLDER'] = 'uploads'

    # Ensure the upload directory exists
    ensure_upload_dir(app.config['UPLOAD_FOLDER'])

    # Enable CORS for all routes
    CORS(app, resources={r"/api/*": {"origins": "http://localhost:8087"}})

    # Initialize extensions
    mongo = PyMongo(app)
    mail = Mail(app)
    jwt = JWTManager(app)

    # Make mongo and mail accessible through the app instance
    app.mongo = mongo
    app.mail = mail

    # Blueprint registration
    from routes import register_blueprints
    register_blueprints(app)

    @app.route('/')
    def index():
        return "Hello, World!"

    return app

def ensure_upload_dir(upload_folder):
    """Ensure the upload directory exists"""
    if not os.path.exists(upload_folder):
        try:
            os.makedirs(upload_folder)
            print(f'Upload directory created at {upload_folder}')
        except Exception as e:
            print(f'Failed to create upload directory {upload_folder}: {e}')
