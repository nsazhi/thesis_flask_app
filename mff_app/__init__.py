from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from mff_app.category import bp as cat_bp

app.register_blueprint(cat_bp, url_prefix='/category')

from mff_app.films import bp as film_bp

app.register_blueprint(film_bp, url_prefix='/films')

from mff_app.admin import bp as adm_bp

app.register_blueprint(adm_bp, url_prefix='/admin')

from mff_app import models
