from app import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=True)
    email = db.Column(db.String, nullable=True)
    password = db.Column(db.String, nullable=True)
    posts = db.relationship("Post", backref="user", lazy=True)
    comments = db.relationship("Comment", backref="user", lazy=True)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password


# para toda classe ou alteração realizada deve-se rodar o comandos no terminal:
#   flask db migrate -m "minha primeira migrate" para gerar as migrations
#   flask db upgrade para gerar as tabelas
# extensões para visualizar o banco sqlite =  sqlite viewer e sqlite
