#from scipy.sparse import data
from werkzeug.datastructures import CombinedMultiDict
from functionality.data_ingestion import Data_Getter
from flask.helpers import make_response, url_for
from flask.wrappers import Response
from werkzeug.utils import redirect
from app_package.forms import TrainingForm, PredictionForm
from flask.templating import render_template
from app_package import app
from flask import render_template,request
import pickle
import pandas as pd
from functionality.models import *
from functionality.data_maker import Data_Maker
from functionality import *


# Homepage
@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home_page.html")


@app.route("/training",methods=["GET","POST"])
def training_page():

    logger_obj = App_Logger()
    log_file = open("log_files/train_log.txt","a")

    form = TrainingForm(request.form)

    if form.validate_on_submit():
        
        # If files are provided using them, and if nothing is provided using default ones
        if (form.data_file.data==None) and (form.data_labels.data==None):
            data_path = "data/dorothea_train.data"
            label_path = "data/dorothea_train.labels"
            # Lets create the files ourselves
            data_file = open(data_path,"r")
            label_file = open(label_path,"r")
        else:
            data_file = form.data_file.data
            label_file = form.data_labels.data
            data_file.save("uploaded_files/data_train_file.txt")
            label_file.save("uploaded_files/label_train_file.txt")
        
        # Lets create the data frames
        data_maker = Data_Maker(data_file,label_file,logger_obj,log_file)
        train_df,train_labels,test_df,test_labels = data_maker.make_data()

        # using the predefined best model for the task
        model = fit_best_model(train_df,train_labels,logger_obj,log_file)

        # Saving the model to use in prediction. It will provide some speeed
        with open("model/best_model.pickle","wb") as f:
            pickle.dump(model,f)

        return redirect(url_for("home_page"))

    elif form.errors != {}:
        for err_msg in form.errors.values():
            print(f"There wan an error with creating user: {err_msg}")

    return render_template("train_page.html",form = form)

#CombinedMultiDict((request.files, request.form))

@app.route("/prediction",methods=["GET","POST"])
def prediction_page():

    # logger obj and updating the existing file
    logger_obj = App_Logger()
    log_file = open("log_files/train_log.txt","a")

    form = PredictionForm(request.form)


    if form.validate_on_submit():
        log_path = "log_files/train_log.txt"
        
        # If files are provided using them, and if nothing is provided using default ones
        if form.data_file.data==None:
            data_path="data/dorothea_test.data"
            data_file = open(data_path,"r")
        else:
            data_file = form.data_file.data
            data_file.save("uploaded_files/data_pred_file.txt")

        
        # Importing the pickle objects of estimator and pca model
        with open("model/best_model.pickle","rb") as f:
            estimator = pickle.load(f)
        with open("model/PCA_obj.pickle","rb") as f:
            pca = pickle.load(f)

        # Random test
        print("PCA Imported")

        # using file to generate data frame 
        data_getter = Data_Getter(data_file,None,logger_obj,log_file)
        data = data_getter.get_data()
        # using pcs model to reduce the data to 500 columns
        data = pca.transform(data)
        data = pd.DataFrame(data)
        
        data.to_csv("uploaded_files/reduced_pred_data.csv")
        # Saved the data file provided in reduced form 

        predictions = predict(estimator,data,logger_obj,log_file)
        predictions = pd.Series(predictions)
        predictions.to_csv("test_labels_generated/predictions.csv")

        # Now i have to produce this file of csv to outside so lets first create one
        file = open("test_labels_generated/predictions.csv","r")

        return Response(file, mimetype="text/csv",
                                   headers={"Content-disposition":
                                              "attachment; filename=predictions.csv"}
                                              )
    return render_template("predict_page.html",form = form)




