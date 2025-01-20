# Blog — My Favorite Films
Интерактивный блог.

Создан в рамках дипломной работы по теме: «Анализ и сравнение написания web-приложений с использованием разных фреймворков».

## Цель проекта
Разработать простое веб-приложение с использованием Flask для сравнения с подобной разработкой на Django и FastAPI.

## Обзор проекта
Веб-приложение на базе фреймворка Flask, которое позволит:
* админстраторам вносить записи в базу данных;
* пользователям просматривать каталог полностью или фильтруя по категориям.

**Фронтенд:** Создан пользовательский интерфейс с использованием Jinja2 – для шаблонов, Bootstrap и CSS – для стилизации.
Для реализации страниц администрирования использованы формы.

**Бэкенд:** Реализована серверная логика с использованием фреймворка Flask.

Настроено подключение к СУБД: по умолчанию SQLite, но с возможностью быстрого подключения любой другой, указанной в файле `.flaskenv`.

Созданы модели для базы данных с помощью Flask-SQLAlchemy.

Настроены миграции с помощью Flask-Migrate.

Настроены маршруты для обработки запросов с помощью Blueprint.

Настроены хэширование паролей (werczeug.security) и логирование администраторов (Flask-Login).

Подключен модуль Flask-WTF для работы с формами.

## Структура проекта
Проект включает в себя следующие ключевые компоненты:

### Домашняя страница
Здесь отображается список всех категорий, имеющихся в базе данных. Каждый пункт — это ссылка на страницу каталога фильмов,содержащая slug категории в динамическом URL для фильтрации.

<img src="https://github.com/nsazhi/thesis_flask_app/blob/master/screenshorts_fl/main_page.jpg">

Рис. 1. Домашняя страница

### Страница каталога
Здесь отображаются карточки фильмов с информацией. В зависимости от параметров запроса, отображается весь каталог фильмов или с фильтрацией по категориям, а также меняется заголовок страницы.
Также на странице есть кнопка выбора фильтра со ссылками, содержащими параметры.

<img src="https://github.com/nsazhi/thesis_flask_app/blob/master/screenshorts_fl/catalog1.jpg">

Рис. 2. Страница полного каталога

#

<img src="https://github.com/nsazhi/thesis_flask_app/blob/master/screenshorts_fl/catalog2.jpg">

Рис. 3. Страница каталога с отбором по категории при переходе с домашней страницы

#

<img src="https://github.com/nsazhi/thesis_flask_app/blob/master/screenshorts_fl/catalog3.jpg">

Рис. 4. Страница каталога с отбором по категории из фильтра

### Панель администратора
Немаловажным для удобства внесения записей в базу данных является наличие панели администратора. Flask не предоставляет возможность генераровать ее автоматически, поэтому для создания страниц администрирования использованы формы.

<img src="https://github.com/nsazhi/thesis_flask_app/blob/master/screenshorts_fl/adm_log_fl.jpg">

Рис. 5. Авторизация админстратора

#

На странице добавления категории есть ссылка на страницу добавления фильма для удобства перемещения между панелями.
Поле `slug` не отображается в форме, а заполняется программно при внесении записи в базу данных.

<img src="https://github.com/nsazhi/thesis_flask_app/blob/master/screenshorts_fl/adm_cat_fl.jpg">

Рис. 6. Добавление категории

#

Поле `img_url` ("Ссылка на изображение"), на случай отсутствия ссылки, заполняется значением по умолчанию для загрузки изображения из статических файлов.

<img src="https://github.com/nsazhi/thesis_flask_app/blob/master/screenshorts_fl/adm_fil_fl.jpg">

Рис. 7. Добавление фильма

#

<img src="https://github.com/nsazhi/thesis_flask_app/blob/master/screenshorts_fl/catalog4.jpg">

Рис. 8. Добавленный фильм с изображением по умолчанию
