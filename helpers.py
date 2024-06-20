import os
from flask_wtf import FlaskForm
from wtforms import validators
from wtforms.fields.simple import StringField


class Formulario_cadastro(FlaskForm):
    nome = StringField('nome',[validators.DataRequired,validators.length(min=1,max=20)])
    email = StringField('email', [validators.DataRequired, validators.length(min=1, max=50)])
    nickname = StringField('nickname', [validators.DataRequired, validators.length(min=1, max=8)])
    senha = StringField('senha', [validators.DataRequired, validators.length(min=1, max=100)])
    salvar = StringField('salvar')