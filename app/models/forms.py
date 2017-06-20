from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextField, BooleanField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField("username", validators=[DataRequired()])
    password = PasswordField("password",validators=[DataRequired()])
    remember_me = BooleanField("remember_me")

class CadastroForm(FlaskForm):
    username = StringField("username", validators=[DataRequired()])
    password = PasswordField("password",validators=[DataRequired()])
    name = TextField("name",validators=[DataRequired()])
    email = TextField("email",validators=[DataRequired()])
