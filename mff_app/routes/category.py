from mff_app.routes import *


# Маршруты с префиксом /category
@app.route('/all', methods=['GET'])
def get_all_categories():
    """
    **Чертеж GET-запроса с префиксом /category:** Список категорий.

    :return: Список всех категорий в базе данных
    """
    categories = db.session.scalars(select(Category)).all()
    return categories


@bp_cat.route('/create', methods=['POST'])
@login_required
def create_category(form):
    """
    **Чертеж POST-запроса с префиксом /category:** Создание категории.

    :raise: Ошибка создания категории

    :return redirect: Текущая страница
    """
    try:
        db.session.execute(insert(Category).values(name=form.name.data,
                                                   slug=slugify(form.name.data)))
        db.session.commit()
        return redirect('#')
    except:
        raise HTTPException('Категория уже существует')
