from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class AddForm(FlaskForm):
    link = StringField('Link', validators=[DataRequired()])
    starred = BooleanField('Starred')
    read = BooleanField('Read')
    dead_link = BooleanField('Dead link')
    header = BooleanField('Header')
    submit = SubmitField('Add link')