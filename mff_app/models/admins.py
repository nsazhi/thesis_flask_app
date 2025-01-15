from typing import Optional
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from mff_app.models import *
from mff_app import login


class Admin(UserMixin, db.Model):
    """
    Создает в базе данных объект модели Администратор.
    """
    __tablename__ = "admins"
    __table_args__ = {"keep_existing": True}
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String(50), unique=True)
    password_hash: Mapped[Optional[str]] = mapped_column(String(256))

    def set_password(self, password):
        """
        Устанавливает хэшированный пароль для объекта модели Admin.

        :param password: Пароль, введенный при регистрации
        :return: Хэш пароля
        """
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """
        Проверяет пароль на соответствие сохраненному хэшу.

        :param password: Пароль, введенный в форме входа `admin/login.html`
        :param password_hash: Сохраненный хэш пароля
        :return bool: Соответствует ли введенный пароль сохраненному
        """
        return check_password_hash(self.password_hash, password)


@login.user_loader
def load_user(id):
    """
    Загружает текущего пользователя.
    """
    return db.session.get(Admin, int(id))
