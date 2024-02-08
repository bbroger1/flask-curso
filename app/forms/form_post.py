from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
from werkzeug.utils import secure_filename
import os


from app.models.post import Post
from app import db, app


class PostForm(FlaskForm):
    text = TextAreaField("Post", validators=[DataRequired()])
    image = FileField("Imagem", validators=[DataRequired()])
    submit = SubmitField("Enviar", validators=[DataRequired()])

    def save(self, user_id):
        image = self.image.data
        secure_name = secure_filename(image.filename)
        post = Post(user_id=user_id, text=self.text.data, image=secure_name)

        image_path = os.path.join(
            os.path.abspath(os.path.dirname((os.path.dirname(__file__)))),
            app.config["UPLOAD_FILES"],
            "post",
            secure_name,
        )
        image.save(image_path)

        db.session.add(post)
        db.session.commit()
