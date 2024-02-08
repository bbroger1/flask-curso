from app import db
from datetime import datetime


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=True)
    text = db.Column(db.String, nullable=True)
    image = db.Column(db.String, nullable=True, default="default.png")
    created = db.Column(db.DateTime, default=datetime.utcnow())
    comments = db.relationship("Comment", backref="post", lazy=True)

    def __init__(self, user_id, text, image):
        self.user_id = user_id
        self.text = text
        self.image = image

    def get_created_formatted(self):
        return self.created.strftime("%d/%m/%Y")


# para toda classe ou alteração realizada deve-se rodar o comandos no terminal:
#   flask db migrate -m "minha primeira migrate" para gerar as migrations
#   flask db upgrade para gerar as tabelas
# extensões para visualizar o banco sqlite =  sqlite viewer e sqlite
