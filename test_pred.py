from functionality.logger import App_Logger
from functionality.models import fit_best_model
from functionality import *
import pickle
from sklearn.metrics import classification_report
import pandas as pd

logger_obj = App_Logger()
log_file = open("log_files/train_log.txt","a")

with open("best_model.pickle","rb") as f:
    estimator = pickle.load(f)

with open("PCA_obj.pickle","rb") as f:
    pca = pickle.load(f)

#reduced_data_file = open("reduced_data_frames/test_df.csv","r")
#label_file = open("reduced_data_frames/test_labels.csv","r")
#reduced_data = pca.transform(data_file)
reduced_train_data = pd.read_csv("reduced_data_frames/train_df.csv",index_col=0)
reduced_train_labels = pd.read_csv("reduced_data_frames/train_labels.csv",index_col=0)
reduced_data = pd.read_csv("reduced_data_frames/test_df.csv",index_col=0)
labels = pd.read_csv("reduced_data_frames/test_labels.csv",index_col=0)

model = fit_best_model(reduced_train_data,reduced_train_labels,logger_obj, log_file)

predictions = estimator.predict(reduced_data)
predictions = pd.DataFrame(predictions)
predictions.to_csv("reduced_data_frames/predictions.csv")

print(classification_report(labels,predictions))
