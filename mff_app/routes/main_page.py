from mff_app.routes import *
from .category import get_all_categories


@app.route('/')
def main_page():
    """
    Главная страница

    **Context**

    ``categories``
        Список объектов `category.Category`.

    :return: 'main.html'
    """
    categories = get_all_categories()
    return render_template('main.html', categories=categories)
