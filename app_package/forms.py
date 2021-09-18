from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FileField
from wtforms.validators import Email, DataRequired
from flask_wtf.file import FileAllowed

#class TrainingForm(FlaskForm):
    #data_file_path = StringField(label="File Path for Training Data")
    #data_labels_path = StringField(label="File Path for Training Data Labels")
    #submit = SubmitField(label="SUBMIT")

#class PredictionForm(FlaskForm):
 #   data_file_path = StringField(label="File Path for Prediction Data")
  #  data_labels_path = StringField(label="File Path for Prediction Data Labels")
   # submit = SubmitField(label="SUBMIT")

class TrainingForm(FlaskForm):
    data_file = FileField('Data File for Training', validators=[FileAllowed(["txt","data","label"])])
    data_labels = FileField('Labels file for training', validators=[FileAllowed(["txt","data","label"])])
    submit = SubmitField(label="TRAIN")

class PredictionForm(FlaskForm):
    data_file = FileField('Data File for Prediction', validators=[FileAllowed(["txt","data","label"])])
    submit = SubmitField(label="PREDICT")