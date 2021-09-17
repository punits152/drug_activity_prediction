# File object 
from functionality.data_ingestion import Data_Getter
from functionality.logger import App_Logger
from sklearn.decomposition import PCA
from functionality.models import *
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import pickle

def get_reduced(X,Y,logger_obj,log_file_obj):
    """
    This function will provide the reduced data in train and test format
    """

    # I will decide between PCA or SparsePCA for reference see notebook
    num_compo = 500
    pca = PCA(n_components=num_compo,random_state=1234,svd_solver="auto")
    X_reduced = pca.fit_transform(X)

    with open("model/PCA_obj.pickle","wb") as f:
        pickle.dump(pca,f)
    logger_obj.log(log_file_obj,"pca model exported")

    explained_variance = np.sum(pca.explained_variance_ratio_)
    logger_obj.log(log_file_obj,f"Successfully reduced dimensions to {num_compo} with total {explained_variance}% of variance explained")

    # Now I will create the train and test data

    X_train, X_test, y_train, y_test = train_test_split(X_reduced,Y,test_size=.20,random_state=123)

    logger_obj.log(log_file_obj,"Train and Test data created")

    return (X_train,X_test,y_train,y_test)

class Data_Maker():
    """
    This class will need the paths of data and label files and 
    produces the dimensionally reduced dataset
    """
    def __init__(self,data_file_path,label_file_path,log_file_path):
        self.data_file_path = data_file_path
        self.label_file_path = label_file_path
        self.log_file_path = log_file_path


    def make_data(self):
        """
        This method will return train_df train_label, test_df, test_label in a tuple use unpacking to get
        the different dataframes in different variables.
        """

        # File for train dataset
        data_file_obj = open(self.data_file_path,"r")

        # file for training data labels
        label_file_obj = open(self.label_file_path,"r")

        # Logger object
        logger_obj = App_Logger()
        # Log file obj
        log_file_obj = open(self.log_file_path,"w")


        # Data getter object for training data frame
        data_getter = Data_Getter(data_file_obj,label_file_obj,logger_obj,log_file_obj)
        df = data_getter.get_data()
        labels = data_getter.get_data_labels()

        ### Here Code goes for reducing data and ten making test and train data
        ## We will decide if its good to have PCA OR SparsePCA
        train_df,test_df,train_labels,test_labels = get_reduced(df,labels,logger_obj,log_file_obj)
        
        train_df = pd.DataFrame(train_df)
        train_df.to_csv("reduced_data_frames/train_df.csv")
        train_labels = pd.DataFrame(train_labels)
        train_labels.to_csv("reduced_data_frames/train_labels.csv")
        test_df = pd.DataFrame(test_df)
        test_df.to_csv("reduced_data_frames/test_df.csv")
        test_labels = pd.DataFrame(test_labels)
        test_labels.to_csv("reduced_data_frames/test_labels.csv")
        

        
        # log all the changes
        logger_obj.log(log_file_obj,"Reduced data sets for train and test are produced successfully")

        return (train_df,train_labels,test_df,test_labels)
