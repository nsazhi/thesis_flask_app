from datetime import date
from mff_app.models import *


class Film(db.Model):
    __tablename__ = "films"
    __table_args__ = {"keep_existing": True}
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(100), unique=True)
    slug: Mapped[str] = mapped_column(String, index=True, unique=True)
    release: Mapped[int] = mapped_column(Integer)
    country: Mapped[str] = mapped_column(String, index=True)
    genre: Mapped[str] = mapped_column(String, index=True)
    director: Mapped[str] = mapped_column(String)
    actors: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String)
    img_url: Mapped[str] = mapped_column(String, default='/static/images/placeholder.png')
    is_viewed: Mapped[bool] = mapped_column(Boolean, index=True, default=False)
    category_id: Mapped[int] = mapped_column(ForeignKey(Category.id), nullable=False, index=True)
    category: Mapped[Category] = relationship(back_populates="films")
    created_at: Mapped[date] = mapped_column(default=lambda: date.today().isoformat())

    def __str__(self):
        return self.title
