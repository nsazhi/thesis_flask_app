from flask import Blueprint
from flask import render_template, jsonify, request, redirect, url_for, flash
from flask_login import login_required

from sqlalchemy import select, insert, update, delete
from werkzeug.exceptions import HTTPException

from mff_app import app, db
from mff_app.models import *
from mff_app.forms import *

from slugify import slugify

# Чертежи
bp_adm = Blueprint('admin', __name__)  # Вход админа - "/admin"
bp_cat = Blueprint('category', __name__)  # Категория - "/category"
bp_fil = Blueprint('films', __name__)  # Фильмы - "/films"

from .main_page import *
from .admins import *
from .category import *
from .films import *
