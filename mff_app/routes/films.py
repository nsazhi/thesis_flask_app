from .category import get_all_categories
from mff_app.routes import *


# Маршруты с префиксом /films
@bp_fil.route('/', methods=['GET'])
def films():
    """
    Получение всех фильмов или списка фильмов по категории при параметре запроса
    """
    slug = request.args.get('slug')
    genre = request.args.get('genre')
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
    Получение списка фильмов по категории - динамические URL
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
    Добавление фильма (для админа)
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
    except:
        raise HTTPException('Фильм уже существует')
