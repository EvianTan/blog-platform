from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    migrate.init_app(app, db)

    from app import routes, models, auth
    app.register_blueprint(routes.bp, url_prefix='/')
    app.register_blueprint(auth.bp, url_prefix='/auth')

    return app
