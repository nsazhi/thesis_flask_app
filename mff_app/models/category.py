from mff_app.models import *


class Category(db.Model):
    __tablename__ = "categories"
    __table_args__ = {"keep_existing": True}
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(50), unique=True)
    slug: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    films: WriteOnlyMapped['Film'] = relationship(back_populates='category')
