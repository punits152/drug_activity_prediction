from scipy.sparse import data
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
    form = TrainingForm(request.form)
    log_path = "log_files/train_log.txt"

    if form.validate_on_submit():
        
        # To get to training even if no file is given
        if (form.data_file.data==None) and (form.data_labels.data==None):
            data_path = "data/dorothea_train.data"
            label_path = "data/dorothea_train.labels"
            # Lets create the files ourselves
            data_file = open(data_path,"r")
            label_file = open(label_path,"r")
        else:
            data_file = form.data_file.data
            label_file = form.data_labels.data
            data_file.save("uploaded_files/data_file.txt")
            label_file.save("uploaded_files/label_file.txt")

            data_file = open("uploaded_files/data_file.txt","r")
            label_file = open("uploaded_files/label_file.txt","r")
        
        # Lets create the data frames
        data_maker = Data_Maker(data_file,label_file,log_path)
        train_df,train_labels,test_df,test_labels = data_maker.make_data()

        # Here will be code for model making

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
        
        #Code goes here
        with open("model/best_model.pickle","rb") as f:
            estimator = pickle.load(f)

        file = open("data/dorothea_test.data","r")

        with open("model/PCA_obj.pickle","rb") as f:
            pca = pickle.load(f)

        data_getter = Data_Getter(file,None,logger_obj,log_file)
        data = data_getter.get_data()
        data = pca.transform(data)
        data = pd.DataFrame(data)
        data.to_csv("data.csv")

        predictions = estimator.predict(data)
        predictions = pd.Series(predictions)
        predictions.to_csv("test_labels_generated/predictions.csv")

        # Now i have to produce this file of csv to outside so lets first create one
        file = open("test_labels_generated/predictions.csv","r")

        return Response(file, mimetype="text/csv",
                                   headers={"Content-disposition":
                                              "attachment; filename=predictions.csv"}
                                              )
    return render_template("predict_page.html",form = form)




