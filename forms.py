from wtforms import Form
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired,Email,EqualTo,Length,NumberRange,regexp
from wtforms import StringField,PasswordField,SubmitField,IntegerField,SelectField,DecimalField



class UserForm(Form):
    matricula = StringField("matricula")
    edad = IntegerField("edad")
    nombre = StringField("Apellidos")
    correo = StringField("correo")
    