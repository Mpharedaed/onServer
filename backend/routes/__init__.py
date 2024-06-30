from .auth import auth_bp
from .posts import posts_bp
from .notifications import notification_bp
from .friendship import friendship_bp
from .user import user_bp
from .profile import profile_bp  # Add this line

def register_blueprints(app):
    app.register_blueprint(auth_bp, url_prefix='/api')
    app.register_blueprint(posts_bp, url_prefix='/api')
    app.register_blueprint(notification_bp, url_prefix='/api')
    app.register_blueprint(friendship_bp, url_prefix='/api')
    app.register_blueprint(user_bp, url_prefix='/api')
    app.register_blueprint(profile_bp, url_prefix='/api')  # Add this line
