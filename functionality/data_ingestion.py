"""
This is a supporting file for the data_maker.py not intended to be used directly
"""
import pandas as pd
import numpy as np

class Data_Getter():
    def __init__(self,data_file_obj,label_file_obj,logger_obj,log_file_obj):
        self.data_file = data_file_obj
        self.logger = logger_obj
        self.log_file = log_file_obj
        self.label_file = label_file_obj

    def get_data(self):
        """ 
        This methods returns the data frame produced for the files of the given format. This provides only the Dataset
        , not the labels
        """
        lines = self.data_file.readlines()

        # Data Creation
        data = []
        for line in lines:
            observation = []
            for item in line.replace("\n","").strip().split(" "):
                observation.append(int(item))
            data.append(observation)

        self.logger.log(self.log_file,"Data Successfully Transformed")

        # Matrix Creation
        matrix=[]
        for observation in data:
            bool_rng = [0 for i in range(0,100000)]
            for item in observation:
                bool_rng[item-1]=1
            matrix.append(bool_rng)

        df = pd.DataFrame(matrix)

        self.logger.log(self.log_file,"DataFrame Successfully Created and Exported")
        
        return df

    def get_data_labels(self):
        """
        This methods returns a labels for the data set provided uses this fixed format.
        """
        # Creating labels
        labels = []
        data_label = self.label_file.read()
        labels_string = data_label.replace("\n",",").strip().split(",")
        labels_string = labels_string[:-1]
        labels_string
        for item in labels_string:
            if int(item) == -1:
                labels.append(0)
            else:
                labels.append(1)

        label_series = pd.Series(labels)
        self.logger.log(self.log_file,"Labels are Successfully Created for train and test")
        return label_series
            