from flask import render_template, request, redirect, url_for, abort, session
from . import main
from .forms import SharePitchForm, UpdateProfile, CommentForm
from flask_login import login_required
from ..models import User, Pitch, Comment
from .. import db, photos


# Views
# Home Page
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its details
    '''
    comment_form = CommentForm()
    
    pitches = Pitch.query.all()
    
    title = 'Minute-Wise'
    return render_template('index.html', title=title, CommentForm=comment_form)

# Share your pitch form
@main.route('/sharePitch', methods=['GET','POST'])
@login_required
def sharePitch():
    '''
    View share_pitch page function that returns the pitch-sharing page and its form
    '''
    posted_pitches = Pitch.query.all()
    form = SharePitchForm()
     
    if form.validate_on_submit():
        pitch = Pitch(pitch = form.pitch.data, category=form.pitch_category.data)
        
        db.session.add(pitch)
        db.session.commit()
        
        return redirect(url_for('main.goToPitches'))
    
    return render_template('new_pitch.html', SharePitchForm=form)

# User profile
@main.route('/user/<usrname>')
def profile(usrname):
    user = User.query.filter_by(username = usrname).first()
    
    if user is None:
        abort(404)
    
    return render_template('/profile/profile.html',user=user)



# Redirect to update profile page
@main.route('/update/<usrname>')
def goToUpdate(usrname):
    
    form = UpdateProfile()
    user = User.query.filter_by(username = usrname).first()
    
    if user is None:
        abort(404)
    
    return render_template('/profile/update.html',user=user,profEditForm = form)


# Update Profile
@main.route('/update/<usrname>', methods=['GET','POST'])
@login_required
def update_profile(usrname):
    
    form = UpdateProfile()
    user = User.query.filter_by(username = usrname).first()
    if user is None:
        abort(404)
    if form.validate_on_submit():
        user.bio = form.bio.data
        
        db.session.add(user)
        db.session.commit()
        
        return redirect(url_for('.profile', usrname=user.username))
    return render_template('/profile/update.html', profEditForm = form)

# Upload prof pic
@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',usrname=uname))


# Comment on other people's pitches
@main.route('/comment', methods=['POST'])
@login_required
def post_comment(pitch):
    '''
    View post_comment function that facilitates posting of comments
    '''
    comment_form = CommentForm()
    comment = Comment.query.filter_by(pitches_id=pitch).first()
    if comment_form.validate_on_submit():
        comment = comment_form.comment.data
        
        db.session.add(comment)
        db.session.commit()
        return render_template('pitches.html', comment=comment)
        
    return render_template('pitches.html', CommentForm=comment_form)


# Redirect to pitches page
@main.route('/pitches')
def goToPitches():
    '''
    View pitches page function that returns the pitches page and its details
    '''   
    catOnePitches = Pitch.query.filter_by(category='Hot & Trending').first()
    catTwoPitches = Pitch.query.filter_by(category='Pick-Up Lines').first()
    catThreePitches = Pitch.query.filter_by(category='Love & Life').first()
    
    categoryOne = Pitch.query.filter_by(category='Hot & Trending').first()
    catTwo = Pitch.query.filter_by(category='Pick-Up Lines').first()
    catThree = Pitch.query.filter_by(category='Love & Life').first()
 

    comment_form = CommentForm()
    
    return render_template('/pitches.html', catOnePitches=catOnePitches, catTwoPitches=catTwoPitches, catThreePitches=catThreePitches, categoryOne=categoryOne, catTwo=catTwo, catThree=catThree, CommentForm=comment_form)