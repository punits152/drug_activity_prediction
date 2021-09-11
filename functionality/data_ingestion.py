import pandas as pd
import numpy as np

class Data_Getter():
    def __init__(self,file_obj,logger_obj,log_file_obj):
        self.file = file_obj
        self.logger = logger_obj
        self.log_file = log_file_obj

    def get_data(self):
        lines = self.file.readlines()

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
            