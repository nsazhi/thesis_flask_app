from typing import Optional
from mff_app.models import *


class Admin(db.Model):
    __tablename__ = "admins"
    __table_args__ = {"keep_existing": True}
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String(50), unique=True)
    password_hash: Mapped[Optional[str]] = mapped_column(String(256))