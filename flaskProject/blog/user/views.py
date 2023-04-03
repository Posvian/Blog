from flask import Blueprint, render_template, redirect
from werkzeug.exceptions import NotFound

from blog.models.user import User

user = Blueprint('user', __name__, url_prefix='/users', static_folder='../static')

# USERS = {
#     1: 'Dima',
#     2: 'Masha',
#     3: 'Alex',
# }


@user.route('/')
def user_list():
    users = User.query.all()
    return render_template(
        'users/list.html',
        users=users,
    )


@user.route('/<int:pk>')
def profile(pk: int):
    user = User.query.filter_by(id=pk).one_or_none()
    if not user:
        raise NotFound(f'User with id {pk} not found')
    return render_template(
        'users/profile.html',
        user=user,
    )
