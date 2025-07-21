from flask_wtf import FlaskForm
from wtforms import StringField, FileField, SubmitField
from wtforms.validators import DataRequired

class ImagePromptForm(FlaskForm):
    prompt = StringField('Prompt', validators=[DataRequired()])
    image = FileField('Reference Image (optional)')
    submit = SubmitField('Generate Image')
