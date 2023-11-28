# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 18:39:42 2023

@author: HP
"""

import pandas as pd

data = {'Name': ['John', 'Mary', 'Bob', 'Sarah', 'Tom', 'Lisa'],
        'Department': ['IT', 'Marketing', 'Sales', 'IT', 'Finance', 'Marketing'],
        'Age': [30, 40, 25, 35, 45, 28],
        'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female'],
        'Salary': [50000, 60000, 45000, 55000, 70000, 55000],
        'Experience': [3, 7, 2, 5, 10, 4]}

employee_df = pd.DataFrame(data)

# --------QUESTION1---------Use the iloc method to select the first 3 rows of the dataframe.
select_1 = employee_df.iloc[:4, :]

# --------QUESTION2---------Use the loc method to select all rows where the Department is "Marketing".
select_2 = employee_df.loc[employee_df["Department"] == "Marketing"]

# --------QUESTION3---------Use the iloc method to select the Age and Gender columns for the first 4 rows of the dataframe.
select_3 = employee_df.iloc[:5, [2, 3]]

# --------QUESTION3---------Use the loc method to select the Salary and Experience columns for all rows where the Gender is "Male".
select_4 = employee_df.loc[employee_df["Gender"] == "Male"]
select_5 = select_4.loc[:, ["Salary", "Experience"]]
