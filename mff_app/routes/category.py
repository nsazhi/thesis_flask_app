from mff_app.routes import *


# Маршруты с префиксом /category
@app.route('/all', methods=['GET'])
def get_all_categories():
    """
    Получение всех категорий из БД
    """
    categories = db.session.scalars(select(Category)).all()
    return categories


@bp_cat.route('/create', methods=['POST'])
@login_required
def create_category(form):
    """
    Добавление категории (для админа)
    """
    try:
        db.session.execute(insert(Category).values(name=form.name.data,
                                                   slug=slugify(form.name.data)))
        db.session.commit()
    except:
        raise HTTPException('Категория уже существует')
