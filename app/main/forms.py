from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required


class CategoryForm(FlaskForm):
    """
    class to create a form to create category
    """
    name = StringField('Pitch Category',validators=[Required()])
    submit = SubmitField('Create')


class PostForm(FlaskForm):
    """
    class to create form to write pitch
    """
    title = StringField('Blog title', validators=[Required()])
    subtitle = StringField('Blog subtitle', validators=[Required()])
    pitch = StringField('Blog Content', validators=[Required()])

    submit = SubmitField('Submit')


class CommentForm(FlaskForm):
    """
    class to create form to comment on a pitch
    """
    comment = StringField('Comment Content', validators=[Required()])
    submit = SubmitField('Submit')


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us more about you...')
    submit = SubmitField('Submit')
