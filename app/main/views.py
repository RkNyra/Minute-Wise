from flask import render_template
from app import app
from .forms import SignUpForm, SignInForm

# Views
# Home Page
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its details
    '''
    
    title = 'Minute-Wise'
    return render_template('index.html', title=title)

# Sign Up Page/Form
@app.route('/signUp')
def signUp():
    form = SignUpForm()
    
    '''
    View sign_up page function that returns the sign_up page and sign_up form
    '''
    return render_template('signUp.html', SignUpForm=form)

# Sign In Page/Form
@app.route('/signIn')
def signIn():
    formLogin = SignInForm()
    
    '''
    View sign_in page function that returns the sign_in page and sign_in form
    '''
    return render_template('signIn.html', SignInForm=formLogin)