# File object 
from functionality.data_ingestion import Data_Getter
from functionality.logger import App_Logger


class Data_Maker():
    """
    This class will need the paths of train data, train labels, test data, test labels
    """
    def __init__(self,train_data_file_path,train_label_file_path,test_data_file_path,test_label_file_path):
        self.train_data_file_path = train_data_file_path
        self.train_label_file_path = train_label_file_path
        self.test_data_file_path = test_data_file_path
        self.test_label_file_path = test_label_file_path

        pass
    def make_data(self):

        # File for train dataset
        train_data_file_obj = open(self.train_data_file_path,"r")

        # file for test dataset
        test_data_file_object = open(self.test_data_file_path,"r")

        # file for training data labels
        train_label_file_obj = open(self.train_label_file_path,"r")

        # file for test data labels
        test_label_file_obj = open(self.test_label_file_path,"r")



        # Logger object
        logger_obj = App_Logger()

        # Log file obj
        log_file_path = "log_files/train_log.txt"
        log_file_obj = open(log_file_path,"w")


        # Data getter object for training data frame
        train_data_getter = Data_Getter(train_data_file_obj,train_label_file_obj,logger_obj,log_file_obj)
        train_df = train_data_getter.get_data()
        train_labels = train_data_getter.get_data_labels()

        # Data getter object for test data frame
        test_data_getter = Data_Getter(test_data_file_object,test_label_file_obj,logger_obj,log_file_obj)
        test_df = test_data_getter.get_data()
        test_labels = test_data_getter.get_data_labels()

        return (train_df,train_labels,test_df,test_labels)
