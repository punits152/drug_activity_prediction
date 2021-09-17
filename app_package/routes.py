from functionality.data_ingestion import Data_Getter
from flask.helpers import url_for
from flask.wrappers import Response
from werkzeug.utils import redirect
from app_package.forms import TrainingForm, PredictionForm
from flask.templating import render_template
from app_package import app
from flask import render_template
import pickle
import pandas as pd
from functionality.models import *
# Needed Information
from functionality.data_maker import Data_Maker
from functionality import *

logger_obj = App_Logger()
log_file = open("log_files/train_log.txt","a")




# Homepage
@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home_page.html")


@app.route("/training",methods=["GET","POST"])
def training_page():
    form = TrainingForm()
    log_path = "log_files/train_log.txt"

    if form.validate_on_submit():
        
        # To get to training even if no file is given
        if (len(form.data_file_path.data)==0) and (len(form.data_labels_path.data)==0):
            data_path = "data/dorothea_train.data"
            label_path = "data/dorothea_train.labels"
        else:
            data_path = form.data_file_path.data
            label_path = form.data_labels_path.data
        
        # Lets create the data frames
        data_maker = Data_Maker(data_path,label_path,log_path)
        train_df,train_labels,test_df,test_labels = data_maker.make_data()

        return redirect(url_for("home_page"))

    elif form.errors != {}:
        for err_msg in form.errors.values():
            print(f"There wan an error with creating user: {err_msg}")

    return render_template("train_page.html",form = form)



@app.route("/prediction",methods=["GET","POST"])
def prediction_page():
    form = PredictionForm()
    if form.validate_on_submit():
        log_path = "log_files/train_log.txt"
        
        if ((len(form.data_file_path.data)==0) and(len(form.data_labels_path.data)==0)):
            data_path="data/dorothea_test.data"
        else:
            data_path = form.data_file_path.data
        
        # Getting the data frame
        data_file_obj = open(data_path,"r")
        data_getter = Data_Getter(data_file_obj,None,logger_obj,log_file)
        data = data_getter.get_data()

        # Getting pca object to convert data
        with open("model/PCA_obj.pickle","rb") as f:
            pca = pickle.load(f)
        
        # Dimensionality reduction
        reduced_data_test = pca.transform(data)
        reduced_data_test = pd.DataFrame(reduced_data_test)


        with open("best_model.pickle","rb") as f:
            estimator = pickle.load(f)

        reduced_train_data = pd.read_csv("reduced_data_frames/train_df.csv",index_col=0)
        reduced_train_labels = pd.read_csv("reduced_data_frames/train_labels.csv",index_col=0)
        
        #these are sets from test split
        #reduced_data = pd.read_csv("reduced_data_frames/test_df.csv",index_col=0)
        #labels = pd.read_csv("reduced_data_frames/test_labels.csv",index_col=0)

        model = fit_best_model(reduced_train_data,reduced_train_labels,logger_obj, log_file)

        predictions = estimator.predict(reduced_data_test)
        predictions = pd.DataFrame(predictions)
        predictions = predictions.to_csv("reduced_data_frames/predictions.csv")

        # Here we will predict the labels and will call it predictions and it will be in csv format
        # it will generate and will use to_csvto generate csv

        return Response(predictions, mimetype="text/csv",
                                        headers={"Content-disposition":
                                                "attachment; filename=predictions.csv"}
                                                )
    return render_template("predict_page.html",form = form)