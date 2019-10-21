from flask import render_template, redirect, url_for
from . import main
from .forms import SharePitchForm
from flask_login import login_required


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
@main.route('/sharePitch')
def sharePitch():
    form = SharePitchForm()
    
    '''
    View share_pitch page function that returns the pitch-sharing page and its form
    '''
    return render_template('/new_pitch.html', SharePitchForm=form)

