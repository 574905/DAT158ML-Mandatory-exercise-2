
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, SelectField, SelectField, RadioField, BooleanField, SubmitField
from wtforms.validators import DataRequired, NumberRange


class DataForm(FlaskForm):

    """
    The form for entering values during patient encounter. Feel free to add additional 
    fields for the remaining features in the data set (features missing in the form 
    are set to default values in `predict.py`).
    """

    budget = IntegerField('Budget: ', validators=[NumberRange(min=0, max=500)])

    genres = StringField('Genre: ', validators=[DataRequired()])

    release_year = IntegerField('Release year: ', validators=[NumberRange(min=1850, max=2020)])

    submit = SubmitField('Submit')