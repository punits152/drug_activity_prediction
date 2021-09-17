"""
Running this file is not intended its for testing only. Training will generally take more time
"""
from functionality.data_maker import Data_Maker
from functionality import *
data_path = "data/dorothea_train.data"
label_path = "data/dorothea_train.labels"
log_path = "log_files/train_log.txt"

data_maker = Data_Maker(data_path,label_path,log_path)
train_df,test_df,train_labels,test_labels = data_maker.make_data()
