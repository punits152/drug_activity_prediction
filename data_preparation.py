# File object 
from functionality.data_ingestion import Data_Getter
from functionality.logger import App_Logger


data_file_path = "data/dorothea_train.data"
file_obj = open(data_file_path,"r")

# Logger object
logger_obj = App_Logger()

# Log file obj
log_file_path = "log_files/train_log.txt"
log_file_obj = open(log_file_path,"w")


# Data getter object
data_getter = Data_Getter(file_obj,logger_obj,log_file_obj)
df = data_getter.get_data()
