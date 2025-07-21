from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Optional

class APIKeysForm(FlaskForm):
    openai_key = StringField("OpenAI API Key", validators=[Optional()])
    shopify_key = StringField("Shopify API Key", validators=[Optional()])
    meta_key = StringField("Meta Ads Access Token", validators=[Optional()])
    smtp_key = StringField("SMTP Email Password", validators=[Optional()])
