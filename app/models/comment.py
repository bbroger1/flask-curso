from app import db
from datetime import datetime


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=True)
    post_id = db.Column(db.Integer, db.ForeignKey("post.id"), nullable=True)
    text = db.Column(db.String, nullable=True)
    created = db.Column(db.DateTime, default=datetime.utcnow())

    def __init__(self, user_id, post_id, text):
        self.user_id = user_id
        self.post_id = post_id
        self.text = text

    def get_created_formatted(self):
        return self.created.strftime("%d/%m/%Y")

    def save(self, user_id, post_id, text):
        try:
            comment = Comment(
                user_id=user_id,
                post_id=post_id,
                text=text,
            )

            db.session.add(comment)
            db.session.commit()

            return True
        except Exception as e:
            print("except l32: ", e)
            return False

    def getComments(self, post_id):
        try:
            return True
        except Exception as e:
            return False


# para toda classe ou alteração realizada deve-se rodar o comandos no terminal:
#   flask db migrate -m "minha primeira migrate" para gerar as migrations
#   flask db upgrade para gerar as tabelas
# extensões para visualizar o banco sqlite =  sqlite viewer e sqlite
