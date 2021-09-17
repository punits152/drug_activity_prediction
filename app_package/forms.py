from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Email, EqualTo, Length

class RegisterForm(FlaskForm):
    username = StringField(label="User Name : ", validators=[Length(min=2,max=30)])
    email_address = StringField(label="Email Address : ",validators=[Email()])
    password1 = PasswordField(label="Password : ", validators=[Length(min=6)])
    password2 = PasswordField(label="Confirm Password : ", validators=[EqualTo("password1")])
    submit = SubmitField(label="Create Account")

class TrainingForm(FlaskForm):
    data_file_path = StringField(label = "File Path for Training Data ")
    data_labels_path = StringField(lable = "File Path for Training Data Labels")
    submit = SubmitField(label="SUBMIT")