import pandas as pd
import pickle
from functionality.logger import App_Logger
from functionality.data_ingestion import Data_Getter


logger_obj = App_Logger()
log_file = open("log_files/train_log.txt","a")
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
predictions.to_csv("predictions.csv")


