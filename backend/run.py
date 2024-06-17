from flask import Flask
from flask_pymongo import PyMongo
from flask_login import LoginManager
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv()

mongo = PyMongo()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['MONGO_URI'] = os.getenv('MONGO_URI')

    if not app.config['MONGO_URI']:
        raise ValueError("MONGO_URI environment variable not set")

    mongo.init_app(app)
    app.mongo = mongo  # Make mongo available globally
    login_manager.init_app(app)

    from app.routes import auth_bp
    app.register_blueprint(auth_bp)

    CORS(app, resources={r"/*": {"origins": "*"}})

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
