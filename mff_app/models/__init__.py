from sqlalchemy import String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, WriteOnlyMapped, relationship
from mff_app import db

from .category import Category
from .films import Film
from .admins import Admin
