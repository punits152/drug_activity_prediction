from flask.wrappers import Response
from werkzeug.utils import redirect
from app_package.forms import TrainingForm, PredictionForm
from flask.templating import render_template
from app_package import app
from flask import render_template

# Needed Information
from functionality.data_maker import Data_Maker
from functionality import *


# Homepage
@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home_page.html")


@app.route("/training",methods=["GET","POST"])
def training_page():
    # this will take time to run 

    """
    Here will be a form that will ask for the path of the file 
    or the file from internet
    data_path = "data/dorothea_train.data"
    label_path = "data/dorothea_train.labels" 
    """
    form = TrainingForm()

    log_path = "log_files/train_log.txt"
    form = TrainingForm()
    if form.validate_on_submit():

        data_path = form.data_file_path.data
        label_path = form.data_labels_path.data
        data_maker = Data_Maker(data_path,label_path,log_path)
        train_df,train_labels,test_df,test_labels = data_maker.make_data()

        return render_template("prediction_page.html",data_frames = (train_df,train_labels,test_df,test_labels))

    elif form.errors != {}:
        for err_msg in form.errors.values():
            print(f"There wan an error with creating user: {err_msg}")

    return render_template("train_page.html",form = form)



@app.route("/prediction",methods=["GET","POST"])
def prediction_page():
    form = PredictionForm()
    if form.validate_on_submit():
        log_path = "log_files/train_log.txt"
        
        data_path = form.data_file_path.data
        label_path = form.data_labels_path.data


        # Here we will predict the labels and will call it predictions and it will be in csv format
        predictions = "" # it will generate and will use to_csvto generate csv

        return Response(predictions)
    return render_template("predict_page.html",form = form)