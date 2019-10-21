from flask import render_template, redirect, url_for
from . import main
from .forms import SignUpForm, SignInForm

# Views
# Home Page
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its details
    '''
    
    title = 'Minute-Wise'
    return render_template('index.html', title=title)

# Sign Up Page/Form
@main.route('/signUp')
def signUp():
    form = SignUpForm()
    
    '''
    View sign_up page function that returns the sign_up page and sign_up form
    '''
    return render_template('signUp.html', SignUpForm=form)

# Sign In Page/Form
@main.route('/signIn')
def signIn():
    formLogin = SignInForm()
    
    '''
    View sign_in page function that returns the sign_in page and sign_in form
    '''
    return render_template('signIn.html', SignInForm=formLogin)