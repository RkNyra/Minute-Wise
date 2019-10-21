from flask import render_template
from . import auth
from .forms import SignUpForm, SignInForm


# Sign Up Page/Form
@auth.route('/signUp')
def signUp():
    form = SignUpForm()
    
    '''
    View sign_up page function that returns the sign_up page and sign_up form
    '''
    return render_template('auth/signUp.html', SignUpForm=form)

# Sign In Page/Form
@auth.route('/signIn')
def signIn():
    formLogin = SignInForm()
    
    '''
    View sign_in page function that returns the sign_in page and sign_in form
    '''
    return render_template('auth/signIn.html', SignInForm=formLogin)