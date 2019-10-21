from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import Required,Email,Length,EqualTo
from wtforms import ValidationError

class SignUpForm(FlaskForm):
    username = StringField('Enter your preferred username', validators=[Required()])
    email = StringField('Enter your email address', validators=[Required(), Email()])
    password = PasswordField('Enter you referred password', validators=[Required(), EqualTo('confirm_password',message = 'Passwords must match')])
    confirm_passowrd = PasswordField('Confirm password', validators=[Required()])
    submit = SubmitField('Sign Up')