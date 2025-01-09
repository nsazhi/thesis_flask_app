from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# Создание приложения
app = Flask(__name__, template_folder="templates")
# Конфигурация приложения
app.config.from_object(Config)
# Создание БД
db = SQLAlchemy(app)
# Создание миграций
migrate = Migrate(app, db)
#
login = LoginManager(app)
login.login_view = 'login'

# Blueprints (Подключение маршрутов)
from mff_app.routes import bp_cat, bp_fil, bp_adm

app.register_blueprint(bp_cat, url_prefix='/category')
app.register_blueprint(bp_fil, url_prefix='/films')
app.register_blueprint(bp_adm, url_prefix='/admin')

from mff_app import models, routes
