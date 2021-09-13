from sklearn.ensemble import AdaBoostClassifier
from functionality.logger import App_Logger
from functionality.data_maker import Data_Maker
from functionality.models import *

logger = App_Logger()
log_file_path = "log_files/train_log.txt"
log_file_obj = open(log_file_path,"w")

def fit_best_model(X,Y,logger,log_file_obj):
    """
    Returns a Adaboost classifier with n_estimators = 300. For more info about model selection see notebook
    I have used GridSearchCV to get the best n_estimators and it gave the best results
    """
    model = AdaBoostClassifier(n_estimators=300,random_state=1234)
    logger.log(log_file_obj,"Created Adaboost model")

    model.fit(X,Y)

    return model 

def predict(model,X,logger,log_file_obj):
    y_hat = model.predict(X)
    logger.log(log_file_obj,"Prediction Completed")
    return y_hat

