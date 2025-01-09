from sqlalchemy import String, Integer, Boolean, Date, ForeignKey
from sqlalchemy.orm import Mapped, WriteOnlyMapped, mapped_column, relationship
from mff_app import db

from .category import Category
from .films import Film
from .admins import Admin
