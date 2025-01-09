from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Войти')


class CategoryForm(FlaskForm):
    name = StringField('Название')
    submit = SubmitField('Готово')


class FilmForm(FlaskForm):
    category_id = StringField('Категория', validators=[Length(min=1)])
    title = StringField('Название')
    release = StringField('Год выхода')
    country = StringField('Страна')
    genre = StringField('Жанр')
    director = StringField('Режиссер')
    actors = StringField('Актеры')
    description = TextAreaField('Описание')
    img_url = StringField('Ссылка на изображение', default='/static/images/placeholder.png')
    submit = SubmitField('Готово')
