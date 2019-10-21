from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import Required,Email,Length,EqualTo
from wtforms import ValidationError

class SignUpForm(FlaskForm):
    username = StringField('', validators=[Required()], render_kw={"placeholder": "Enter your preferred username"})
    email = StringField('', validators=[Required(), Email()], render_kw={"placeholder": "Enter your email address"})
    password = PasswordField('', validators=[Required(), EqualTo('confirm_password',message = 'Passwords must match')], render_kw={"placeholder": "Enter your referred password"})
    confirm_passowrd = PasswordField('', validators=[Required()], render_kw={"placeholder": "Confirm password"})
    submit = SubmitField('Sign Up')
    
    
class SignInForm(FlaskForm):
    email = StringField('', validators=[Required(), Email()], render_kw={"placeholder": "Enter your email address"})
    password = PasswordField('', validators=[Required()], render_kw={"placeholder": "Enter your password"})
    remember = BooleanField('Keep me signed in')
    submit = SubmitField('Sign In')