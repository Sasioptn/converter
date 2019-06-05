from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired


class DownloadForm(FlaskForm):
    link = StringField('Put your link here ',validators=[DataRequired()])
    submit = SubmitField('Скачать')