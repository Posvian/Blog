from flask import Blueprint, render_template
from flask_login import login_required

from blog.models import User

article = Blueprint('article', __name__, url_prefix='/articles', static_folder='../static')

ARTICLES = {
    1: {
        'title': 'Want to eat)))',
        'text': 'Want to eat!!!',
        'author': 1},
    2: {
        'title': 'My love',
        'text': 'I love Dima!!!',
        'author': 2},
    3: {
        'title': 'My dream!))',
        'text': 'Want to sleep!))',
        'author': 3},
}


@article.route('/')
@login_required
def article_list():
    return render_template(
        'articles/list.html',
        articles=ARTICLES,
    )


@article.route('<int:pk>')
def get_article(pk: int):
    article_title = ARTICLES[pk]['title']
    article_text = ARTICLES[pk]['text']
    user_id = ARTICLES[pk]['author']
    # article_author = USERS[ARTICLES[pk]['author']]
    article_author = User.query.filter_by(id=ARTICLES[pk]['author']).one_or_none()
    if not article_author:
        article_author = 'Автор неизвестен'
    return render_template(
        'articles/detail.html',
        article_title=article_title,
        article_text=article_text,
        article_author=article_author,
        user_id=user_id
    )
