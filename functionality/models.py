from sklearn.ensemble import AdaBoostClassifier
from functionality.logger import App_Logger
from functionality.models import *
import pickle


def fit_best_model(X,Y,logger_obj,log_file_obj):
    """
    Returns a Adaboost classifier with n_estimators = 300. For more info about model selection see notebook
    I have used GridSearchCV to get the best n_estimators and it gave the best results
    """
    model = AdaBoostClassifier(n_estimators=300,random_state=1234)
    logger_obj.log(log_file_obj,"Created Adaboost model")

    model.fit(X,Y)
    logger_obj.log(log_file_obj,"Training Completed")

    with open("model/best_model.pickle","wb") as f:
        pickle.dump(model,f)

    return model 

def predict(model,X,logger_obj,log_file_obj):
    y_hat = model.predict(X)
    logger_obj.log(log_file_obj,"Prediction Completed")
    return y_hat

