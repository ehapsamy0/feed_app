from flask import Flask
from app.db_config import close_db
from app.routes import post_bp

def create_app():
    app = Flask(__name__)

    # Register the blueprint
    app.register_blueprint(post_bp)

    # Close DB connection
    app.teardown_appcontext(close_db)

    return app
