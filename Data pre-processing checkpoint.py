
import numpy as np
import pandas as pd

data = "C:/Users/HP/Downloads/STEG_BILLING_HISTORY.csv"
dataset = pd.read_csv(data)

# --------------Question1-----------------
# Load the dataset, display the ten first lines, store the results in a variable called 'client_0_bills'.
client_0_bills = dataset.head(11)

# --------------Question2-----------------
# What is the data type of the 'client_0_bills' variable ?
# Answer = Dataframe

# --------------Question3-----------------
# Display the general information of the dataset and try to answer the following questions :
    # 1) How many rows and columns do we have in this dataset ?
# Answer = "4476749" rows and "16" columns

    # 2) How many categorical features are present in the dataset ?
Categorical_data = dataset.dtypes.value_counts()
# Answer = "4"

    # 3) How much memory space does the dataset consume ?
data_mem = dataset.memory_usage(index = True).sum()
# Answer = "573024004"

# --------------Question4-----------------
# Inspect the dataset for potential missing values.
inspect_data = pd.isna(dataset)

# --------------Question5-----------------
# Select your strategy to handle missing values, and tell us why you had made that choice.
drop_missing_row = dataset.dropna()# I droped any row that has a missing value cause i didnt want it to affect the normal distribution of the graph

# --------------Question6-----------------
# Run a descriptive analysis on numeric features (columns).
dataset_descriptive_statistics = dataset.describe()

# --------------Question7-----------------
# Select the bills records for the client with an id ='train_Client_0', using 2 methods.
select_1 = dataset.loc[dataset["client_id"] == "train_Client_0"]

# --------------Question8-----------------
# Transform the 'counter_type' feature to a numeric variable using the encoder of your choice.
transform_data = dataset["counter_type"].replace(["ELEC", "GAZ"],  # using .replace() method
                                                 [0, 1], inplace=True)

# --------------Question9-----------------
# Delete the 'counter_statue' feature from the Dataframe
drop_data = dataset.drop("counter_statue", axis = 1)










