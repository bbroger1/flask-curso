from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email

from app.models.user import User
from app import bcrypt


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Senha", validators=[DataRequired()])
    submit = SubmitField("Enviar", validators=[DataRequired()])

    def login(self):
        user = None
        user = User.query.filter_by(email=self.email.data).first()

        if user:
            if bcrypt.check_password_hash(
                user.password, self.password.data.encode("utf-8")
            ):
                return user
            else:
                raise Exception("Dados incorretos [1]")
        else:
            raise Exception("Dados incorretos [2]")
