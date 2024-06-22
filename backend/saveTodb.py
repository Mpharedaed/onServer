import os
import sys

# Ensure the 'backend/app' directory is in the sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), 'app'))

from flask import Flask, current_app
from flask_pymongo import PyMongo
from models import Post
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.config['MONGO_URI'] = os.getenv('MONGO_URI')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

mongo = PyMongo(app)

with app.app_context():
    app.mongo = mongo

    # Create a test post
    test_post = Post(
        user_id="test_user_id",
        content="This is a test post",
        tags=["test", "post"],
        image_url="http://example.com/image.png"
    )

    # Save the post to the database
    success = test_post.save_to_db()

    if success:
        print("Test post saved successfully")
    else:
        print("Failed to save test post")

    # Retrieve and print all posts to verify insertion
    posts = Post.get_all_posts()
    for post in posts:
        print(post.__dict__)
