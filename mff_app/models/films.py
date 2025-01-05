from datetime import date

from sqlalchemy import String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from mff_app import db
from mff_app.models import *


class Film(db.Model):
    __tablename__ = "films"
    __table_args__ = {"keep_existing": True}
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(100), unique=True)
    slug: Mapped[str] = mapped_column(String(200), index=True, unique=True)
    release: Mapped[int] = mapped_column(Integer)
    country: Mapped[str] = mapped_column(String, index=True)
    genre: Mapped[str] = mapped_column(String, index=True)
    director: Mapped[str] = mapped_column(String)
    actors: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String)
    img_url: Mapped[str] = mapped_column(String)
    is_viewed: Mapped[bool] = mapped_column(Boolean, index=True, default=False)
    category_id: Mapped[int] = mapped_column(ForeignKey(Category.id), nullable=False, index=True)
    category: Mapped[Category] = relationship(back_populates="films")
    created_at: Mapped[date] = mapped_column(default=lambda: date.today().isoformat())
