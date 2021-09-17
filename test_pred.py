from functionality import *
import pickle
import pandas as pd

with open("best_model.pickle","rb") as f:
    estimator = pickle.load(f)

with open("PCA_obj.pickle","rb") as f:
    pca = pickle.load(f)

reduced_data_file = open("reduced_data_frames/test_df.csv","r")
label_file = open("reduced_data_frames/test_labels.csv","r")
#reduced_data = pca.transform(data_file)


predictions = estimator.predict(reduced_data_file)
predictions = pd.DataFrame(predictions)
predictions.to_csv("reduced_data_frames/predictions.csv")