from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError

from app.models.user import User
from app import db, bcrypt


class UserForm(FlaskForm):
    name = StringField("Nome", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Senha", validators=[DataRequired()])
    confirm_password = PasswordField(
        "Senha", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("Salvar", validators=[DataRequired()])

    def validate_email(self, email):
        if User.query.filter_by(email=email.data).first():
            return ValidationError("Usuário já cadastrado.")

    def save(self):
        password_hash = bcrypt.generate_password_hash(
            self.password.data.encode("utf-8")
        )
        user = User(
            name=self.name.data,
            email=self.email.data,
            password=password_hash,
        )

        db.session.add(user)
        db.session.commit()

        return user
