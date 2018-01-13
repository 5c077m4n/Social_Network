from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import (DataRequired, Regexp, ValidationError,
								Email, Length, EqualTo)

from models import User


def name_exists(FlaskForm, field):
    if User.select().where(User.username == field.data).exists():
        raise ValidationError('This username is already taken.')


def email_exists(FlaskForm, field):
    if User.select().where(User.email == field.data).exists():
        raise ValidationError('This email is already taken.')


class RegistarationForm(FlaskForm):
    username = StringField(
        'Username',
        validators = [
            DataRequired(),
            Regexp(
                r'^[a-zA-Z0-9]+$',
                message = "The username should be one word with letters,"
                + " numbers, and underscores only."
            ),
            name_exists
        ]
    )
    email = StringField(
        'E-mail',
        validators = [
            DataRequired(),
            Email(),
            email_exists
        ]
    )
    password = PasswordField(
        'Password',
        validators = [
            DataRequired(),
            Length(min = 5, message = 'Your password must be at least 5 characters long.'),
        ]
    )
    password2 = PasswordField(
        'Confirm Password',
        validators = [
            DataRequired(),
            EqualTo('password', message = 'The two passwords must match.')
        ]
    )


class LoginForm(FlaskForm):
    email = StringField('E-mail', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])


class PostForm(FlaskForm):
    content = TextAreaField("Type your post into here:", validators = [DataRequired()])