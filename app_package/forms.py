from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Email, EqualTo, Length

class TrainingForm(FlaskForm):
    data_file_path = StringField(label="File Path for Training Data")
    data_labels_path = StringField(label="File Path for Training Data Labels")
    submit = SubmitField(label="SUBMIT")

class PredictionForm(FlaskForm):
    data_file_path = StringField(label="File Path for Prediction Data")
    data_labels_path = StringField(label="File Path for Prediction Data Labels")
    submit = SubmitField(label="SUBMIT")