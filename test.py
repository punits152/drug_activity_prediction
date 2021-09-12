from functionality.data_maker import Data_Maker

# Now this simple snippet will do all the task for you to train test split 
# Now all you have to do is just fit the models and predict. But it will take some time to do all the work
data_file_path = "data/dorothea_train.data"
label_file_path = "data/dorothea_train.labels"

data_maker = Data_Maker(data_file_path,label_file_path)
X_train,X_test,y_train,y_test = data_maker.make_data()