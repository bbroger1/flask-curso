from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email

from app.models.contact import Contact
from app import db


class ContactForm(FlaskForm):
    name = StringField("Nome", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    subject = StringField("Assunto", validators=[DataRequired()])
    message = TextAreaField("Mensagem", validators=[DataRequired()])
    submit = SubmitField("Enviar", validators=[DataRequired()])

    def save(self):
        contact = Contact(
            name=self.name.data,
            email=self.email.data,
            subject=self.subject.data,
            message=self.message.data,
        )

        db.session.add(contact)
        db.session.commit()
