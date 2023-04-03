from werkzeug.security import generate_password_hash

from blog.app import create_app, db

app = create_app()


@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('done!')


@app.cli.command('create-user')
def create_user():
    from blog.models import User

    db.session.add(
        User(email='posv@mail.ru', password=generate_password_hash('1234'))
    )
    db.session.commit()

    print('done! create user.')
