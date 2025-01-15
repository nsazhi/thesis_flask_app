from flask_login import current_user, login_user
from .category import create_category
from .films import create_film
from mff_app.routes import *


@bp_adm.route('/login', methods=['GET', 'POST'])
def login():
    """
    **Чертеж GET и POST запросов с префиксом /admin:** Форма входа администратора.

    :return: 'admin.login', если GET-запрос и еще не авторизован

    :return redirect: `admin.cat_panel`, если авторизован
    """
    if current_user.is_authenticated:
        return redirect(url_for('admin.cat_panel'))
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.scalar(
                select(Admin).where(Admin.username == form.username.data))
        if user is None or not user.check_password(form.password.data):
            return redirect(url_for('admin.login'))
        login_user(user)
        return redirect(url_for('admin.cat_panel'))
    return render_template('admin/login.html', form=form)


@bp_adm.route('/cat/panel', methods=['GET', 'POST'])
@login_required
def cat_panel():
    """
    **Чертеж GET и POST запросов с префиксом /admin:** Создание категории.

    :raise: Ошибка валидации данных в форме

    :return: `admin.cat_panel`
    """
    form = CategoryForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            create_category(form)
            return redirect(url_for('admin.cat_panel'))
        else:
            raise HTTPException('Error form validation')
    else:
        form = CategoryForm()
    return render_template('admin/cat_panel.html', form=form)


@bp_adm.route('/films/panel', methods=['GET', 'POST'])
@login_required
def film_panel():
    """
    **Чертеж GET и POST запросов с префиксом /admin:** Создание фильма.

    :raise: Ошибка валидации данных в форме

    :return: 'admin.film_panel'
    """
    form = FilmForm()
    print(form)
    if request.method == 'POST':
        if form.validate_on_submit():
            create_film(form)
            return redirect(url_for('admin.film_panel'))
        else:
            raise HTTPException('Error form validation')
    else:
        form = FilmForm()
    return render_template('admin/film_panel.html', form=form)
