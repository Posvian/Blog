from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import logout_user, LoginManager, login_required, login_user
from werkzeug.security import check_password_hash

from blog.models import User

auth = Blueprint('auth', __name__, static_folder='../static')

login_manager = LoginManager()
login_manager.login_view = 'auth.login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).one_or_none()


@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('auth.login'))


__all__ = [
    'load_user',
    'auth',
]


@auth.route('/login', methods=['POST', 'GET'], endpoint='login')
def login():
    if request.method == 'GET':
        return render_template(
            'auth/login.html',
        )
    email = request.form.get('email')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        flash('Check your login details')
        return redirect(url_for('.login'))
    login_user(user)
    return redirect(url_for('user.profile', pk=user.id))


@auth.route('/logout', endpoint='logout')
def logout():
    logout_user()
    return redirect(url_for('.login'))


@auth.route('/secret')
@login_required
def secret_view():
    return 'Super secret data'
