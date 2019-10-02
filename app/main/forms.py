from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,ValidationError, SelectField, RadioField
from wtforms.validators import Required,Email
from ..models import User


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class CommentsForm(FlaskForm):
    comment = TextAreaField('Comment', validators=[Required()])
    submit = SubmitField('SUBMIT')   

class BlogForm(FlaskForm):
    content = TextAreaField('YOUR BLOG')
    submit = SubmitField('Create Blog')

