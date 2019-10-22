from flask import render_template, request, redirect, url_for, abort
from . import main
from .forms import SharePitchForm
from flask_login import login_required
from ..models import User


# Views
# Home Page
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its details
    '''
    
    title = 'Minute-Wise'
    return render_template('index.html', title=title)

# Share your pitch form
@main.route('/sharePitch', methods=['GET','POST'])
@login_required
def sharePitch():
    form = SharePitchForm()
    
    '''
    View share_pitch page function that returns the pitch-sharing page and its form
    '''
    return render_template('/new_pitch.html', SharePitchForm=form)

# User profile
@main.route('/user<usrname>')
def profile(usrname):
    user = User.query.filter_by(username = usrname).first()
    
    if user is None:
        abort(404)
    
    return render_template('profile/profile.html', user = user)
