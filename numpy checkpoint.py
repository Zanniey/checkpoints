

import numpy as np

# Create the grades array
grades = np.array([85, 90, 88, 92, 95, 80, 75, 98, 89, 83])

# Calculate mean, median, and standard deviation
mean_grade = np.mean(grades)
median_grade = np.median(grades)
std_deviation = np.std(grades)

# Find maximum and minimum grades
max_grade = np.max(grades)
min_grade = np.min(grades)

# Sort grades in ascending order
sorted_grades = np.sort(grades)

# Find the index of the highest grade
index_highest_grade = np.argmax(grades)

# Count the number of students who scored above 90
above_90_count = np.sum(grades > 90)

# Calculate the percentage of students who scored above 90
above_90_percentage = (above_90_count / len(grades)) * 100

# Calculate the percentage of students who scored below 75
below_75_percentage = np.sum(grades < 75) / len(grades) * 100

# Extract grades above 90 into a new array
high_performers = grades[grades > 90]

# Create an array of passing grades (above 75)
passing_grades = grades[grades > 75]

# Print the results
print("Grades:", grades)
print("Mean:", mean_grade)
print("Median:", median_grade)
print("Standard Deviation:", std_deviation)
print("Maximum Grade:", max_grade)
print("Minimum Grade:", min_grade)
print("Sorted Grades:", sorted_grades)
print("Index of Highest Grade:", index_highest_grade)
print("Number of Students Above 90:", above_90_count)
print("Percentage of Students Above 90:", above_90_percentage, "%")
print("Percentage of Students Below 75:", below_75_percentage, "%")
print("High Performers:", high_performers)
print("Passing Grades:", passing_grades)
