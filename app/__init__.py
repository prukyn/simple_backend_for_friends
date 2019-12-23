import os

from flask import Flask
from flask_cors import CORS, cross_origin

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile('config.py', silent=True)
    cors = CORS(app)

    from app import db

    with app.app_context():
        db.init_db()

    from app import views

    app.register_blueprint(views.bp)

    return app
