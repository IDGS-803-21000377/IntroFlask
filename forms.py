from wtforms import Form
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired,Email,EqualTo,Length,NumberRange,regexp
from wtforms import StringField,PasswordField,EmailField,SubmitField,IntegerField,SelectField,DecimalField
from wtforms import validators


class UserForm(Form):
    matricula = StringField("matricula",[
        validators.DataRequired("este es un campo requerido"),
        validators.Length(min=2,max=10, message="La matricula debe ser entre ")
    ])
    edad = IntegerField("edad",[
        validators.DataRequired("Este campo es requerido")

    ])
    nombre = StringField("nombre",[
        validators.DataRequired("Este campo es requerido")

    ])
    correo = EmailField("correo",[
        validators.Email(message="Este campo es requerido")

    ])
    apellidos = StringField("Apellidos",[
        validators.DataRequired("Este campo es requerido")

    ])
