from .category import get_all_categories
from mff_app.routes import *


# Маршруты с префиксом /films
@bp_fil.route('/', methods=['GET'])
def films():
    """
    **Чертеж GET-запроса с префиксом /films:** Список всех фильмов или по категории.

    **Если есть параметр запроса:**

    :param: `slug`

    **Context**

    ``category``
        Объект category.Category с Category.slug == slug

    ``films``
        Список объектов `films.Film` с фильтром по Film.category_id.

    :return: Шаблон `films/films_by_category.html`

    **Если нет параметра запроса:**

    **Context**

    ``films``
        Список объектов `films.Film`.

    :return: Шаблон `films/films.html`,
    """
    slug = request.args.get('slug')
    categories = get_all_categories()
    if slug:
        for c in categories:
            if c.slug == slug:
                films = db.session.scalars(select(Film).where(Film.category_id == c.id)).all()
                print(films)
                return render_template('films/films_by_category.html',
                                       categories=categories,
                                       category=c,
                                       films=films)
    else:
        films = db.session.scalars(select(Film)).all()
        return render_template('films/films.html',
                               categories=categories, films=films)


@bp_fil.route('/<category_slug>', methods=['GET'])
def get_films_by_category(category_slug: str):
    """
    **Чертеж GET-запроса с префиксом /films:** Список фильмов по категории.

    :param: `category_slug`

    **Context**

    ``category``
        Объект category.Category с Category.slug == category_slug

    ``films``
        Список объектов `films.Film` с фильтром по Film.category_id.

    :return: Шаблон `films/films_by_category.html`
    """
    categories = get_all_categories()
    for c in categories:
        if c.slug == category_slug:
            films = db.session.scalars(select(Film).where(Film.category_id == c.id)).all()
            return render_template('films/films_by_category.html',
                                   categories=categories,
                                   category=c,
                                   films=films)


@bp_fil.route('/create', methods=['POST'])
@login_required
def create_film(form):
    """
    **Чертеж POST-запроса с префиксом /films:** Создание фильма.

    :raise: Ошибка создания фильма

    :return redirect: Текущая страница
    """
    print(form)
    try:
        db.session.execute(insert(Film).values(title=form.title.data,
                                               slug=slugify(form.title.data),
                                               release=form.release.data,
                                               country=form.country.data,
                                               genre=form.genre.data,
                                               director=form.director.data,
                                               actors=form.actors.data,
                                               description=form.description.data,
                                               img_url=form.img_url.data,
                                               category_id=form.category_id.data,
                                               )
                           )
        db.session.commit()
        return redirect('#')
    except:
        raise HTTPException('Что-то пошло не так')
