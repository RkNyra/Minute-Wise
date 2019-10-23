from flask_wtf import FlaskForm
from wtforms import SelectField,StringField,TextAreaField,SubmitField
from wtforms.validators import Required
from wtforms import ValidationError

class SharePitchForm(FlaskForm):
    # pitch_category = StringField('', validators=[Required()], render_kw={"placeholder": "Select pitch category"})
    
    # select option
    pitch_category = SelectField(' Pitch here!', choices=[('hot', 'Hot & Trending'), ('pl','Pick-up Lines'), ('ll', 'Love & Life')], validators=[Required()])
    
    pitch = TextAreaField('', validators=[Required()], render_kw={"placeholder": "Write your pitch here :)"})
    # contributor_name = StringField('', validators=[Required()], render_kw={"placeholder":"Write your username"})
    # username should pick from current user's username
    submit = SubmitField('Share')


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you',validators=[Required()])
    submit = SubmitField('Update')

class CommentForm(FlaskForm):
    comment = TextAreaField('Your thought?',validators=[Required()], render_kw={"placeholder": "Post your comment"})
    submit = SubmitField('Post Comment')