from flask import render_template,redirect,url_for,flash,request
from flask_login import login_user,logout_user,login_required
from . import auth
from .forms import SignUpForm, SignInForm
from ..models import User
from .. import db


# Sign Up Page/Form
@auth.route('/signUp')
def signUp():
    form = SignUpForm()
    
    '''
    View sign_up page function that returns the sign_up page and sign_up form
    '''
    if form.validate_on_submit():
        user = User(username = form.username.data, email = form.email.data, password = form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.signIn'))
    
    title = "New Pitcher"
    return render_template('auth/signUp.html', SignUpForm=form, title=title)


# Sign In Page/Form
@auth.route('/signIn',methods=['GET', 'POST'])
def signIn():
    formLogin = SignInForm()
    
    '''
    View sign_in page function that returns the sign_in page and sign_in form
    '''
    if formLogin.validate_on_submit():
        user = User.query.filter_by(username = formLogin.username.data).first()
        if user is not None and user.verify_password(formLogin.password.data):
            login_user(user,formLogin.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid username or password')
        
    title = "Minute Wise Login"
    return render_template('auth/signIn.html', SignInForm=formLogin, title=title)

# Sign out page
@auth.route('/signOut')
@login_required
def logOut():
    logout_user()
    return redirect(url_for('main.index'))