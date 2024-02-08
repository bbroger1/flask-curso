from app import db, login_manager
from flask_login import UserMixin
from datetime import datetime

from app.models.user import User


class Contact(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=True)
    email = db.Column(db.String, nullable=True)
    subject = db.Column(db.String, nullable=True)
    message = db.Column(db.String, nullable=True)
    answered = db.Column(db.Integer, default=0)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, name, email, subject, message):
        self.name = name
        self.email = email
        self.subject = subject
        self.message = message


# para toda classe ou alteração realizada deve-se rodar o comandos no terminal:
#   flask db migrate -m "minha primeira migrate" para gerar as migrations
#   flask db upgrade para gerar as tabelas
# extensões para visualizar o banco sqlite =  sqlite viewer e sqlite
