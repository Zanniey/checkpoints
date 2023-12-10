# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 18:16:57 2023

@author: User
"""

#Create a numpy array called "grades" that contains the following grades: [85, 90, 88, 92, 95, 80, 75, 98, 89, 83]

"""Instructions
Create a new file called "grades_analysis.py"
Import the numpy library and create the "grades" array as specified above.
Use numpy functions to calculate the mean, median, and standard deviation of the grades.
Use numpy function to find the maximum and minimum of the grades.
Use numpy function to sort the grades in ascending order.
Use numpy function to find the index of the highest grade in the array.
Use numpy function to count the number of students who scored above 90.
Use numpy function to calculate the percentage of students who scored above 90.
Use numpy function to calculate the percentage of students who scored below 75.
Use numpy function to extract all the grades above 90 and put them in a new array called "high_performers".
Create a new array called "passing_grades" that contains all the grades above 75.
Print the result of all the above steps.
Note:

to calculate percentage use numpy.mean(grades > 90) * 100
to extract the grades above 90 use grades[grades > 90]
to extract the grades above 75 use grades[grades > 75]"""
# grades_analysis.py

import numpy as np

# Create the "grades" array
grades = np.array([85, 90, 88, 92, 95, 80, 75, 98, 89, 83])

# Calculate mean, median, and standard deviation
mean_grade = np.mean(grades)
median_grade = np.median(grades)
std_dev_grade = np.std(grades)

# Find maximum and minimum grades
max_grade = np.max(grades)
min_grade = np.min(grades)

# Sort the grades in ascending order
sorted_grades = np.sort(grades)

# Find the index of the highest grade
index_highest_grade = np.argmax(grades)

# Count the number of students who scored above 90
above_90_count = np.sum(grades > 90)

# Calculate the percentage of students who scored above 90
above_90_percentage = np.mean(grades > 90) * 100

# Calculate the percentage of students who scored below 75
below_75_percentage = np.mean(grades < 75) * 100

# Extract grades above 90 into a new array "high_performers"
high_performers = grades[grades > 90]

# Create a new array "passing_grades" containing grades above 75
passing_grades = grades[grades > 75]

# Print the results
print("Mean Grade:", mean_grade)
print("Median Grade:", median_grade)
print("Standard Deviation of Grades:", std_dev_grade)
print("Maximum Grade:", max_grade)
print("Minimum Grade:", min_grade)
print("Sorted Grades:", sorted_grades)
print("Index of Highest Grade:", index_highest_grade)
print("Number of Students Scoring Above 90:", above_90_count)
print("Percentage of Students Scoring Above 90:", above_90_percentage)
print("Percentage of Students Scoring Below 75:", below_75_percentage)
print("High Performers:", high_performers)
print("Passing Grades (Above 75):", passing_grades)
