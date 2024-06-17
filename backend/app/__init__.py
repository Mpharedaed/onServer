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
    app.config.from_object('config.Config')

    mongo.init_app(app)
    login_manager.init_app(app)

    from app.routes import auth_bp
    app.register_blueprint(auth_bp)

    CORS(app)

    return app
