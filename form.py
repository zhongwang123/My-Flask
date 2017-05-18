from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, SubmitField, 
    PasswordField, IntegerField)
from wtforms import ValidationError
from wtforms.validators import Required, EqualTo
from model import User

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[Required()])
    password = PasswordField('password', validators=[Required()])
    remember_me = BooleanField('keep me logged in')
    submit = SubmitField('submit')

class RegisterForm(FlaskForm):
    username = StringField('User Name', validators=[Required()])
    email = StringField('Email', validators=[Required()])
    password = PasswordField('Password', validators=[
        Required(), EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField('Confirm password', validators=[Required()])
    submit = SubmitField('Register!')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered')
    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use')

