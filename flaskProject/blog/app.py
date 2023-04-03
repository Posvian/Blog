from flask import Flask
from flask_login import LoginManager

from blog.models.database import db
from blog.article.views import article
from blog.user.views import user
from blog.auth.views import auth, login_manager



def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '5os1pc=tyt0%0(krtl_^v4lj_9r2!3ymv1e_-95y-t5g7hk@q2'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    db.init_app(app)

    register_blueprints(app)

    login_manager.init_app(app)

    return app


def register_blueprints(app: Flask):
    app.register_blueprint(user)
    app.register_blueprint(article)
    app.register_blueprint(auth)

