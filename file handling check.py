# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 18:25:44 2023

@author: User
"""

import numpy as np
import pandas as pd
from io import stringIO

# METHOD 1 - Using Numpy genfromtxt()
data =np.genfromtxt(c:\Users\User\"downloads/loan_prediction_dataset.csv")
        # NUMPY has 2 ways of opening a file
            # 1) np.genfromtxt()
            # 2) np.loadtxt()

dataset1 = np.genfromtxt(data, delimiter = ",", skip_header = 1)



# METHOD 2 - Using Numpy loadtxt()
dataset2 = np.loadtxt(data, delimiter = ",", skiprows = 1)



# METHOD 3 - Using Pandas
dataset3 = pd.read_csv(data)



# METHOD 3 - Using the Open() function
with open(data) as dataframe:
    print(dataframe.read())
    dataframe.close()
