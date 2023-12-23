# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 19:20:16 2023

@author: User
"""

#Load the dataset into a data frame using Python.
#Clean the data as needed.
#Plot a line chart to show the average temperature fluctuations in Tunisia and Cameroon. Interpret the results.
#Zoom in to only include data between 1980 and 2005, try to customize the axes labels.
#Create Histograms to show temperature distribution in Senegal between [1980,2000] and [2000,2023] (in the same figure). Describe the obtained results.
#Select the best chart to show the Average temperature per country.
#Make your own questions about the dataset and try to answer them using the appropriate visuals.
 

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset into a data frame
df =pd.read_csv('Africa_climate_change.csv')
# Clean the data as needed (replace "Year", "Country", and "Temperature" with your actual column names)
df['Year'] = pd.to_datetime(df['Year'], errors='coerce')

# Plot a line chart for Tunisia and Cameroon
fig, ax = plt.subplots(figsize=(10, 6))

# Filter data for Tunisia and Cameroon
subset_df = df[df['Country'].isin(['Tunisia', 'Cameroon'])]

# Filter data for the years between 1980 and 2005
subset_df = subset_df[(subset_df['Year'] >= '1980-01-01') & (subset_df['Year'] <= '2005-12-31')]

# Group by country and calculate the average temperature for each year
avg_temp_by_country = subset_df.groupby(['Country', subset_df['Year'].dt.year])['Temperature'].mean().unstack()

# Plot the line chart
avg_temp_by_country.plot(ax=ax, marker='o')
plt.title('Average Temperature Fluctuations (1980-2005)')
plt.xlabel('Year')
plt.ylabel('Average Temperature')
plt.legend(title='Country')
plt.show()
# Plot histograms for Senegal between [1980,2000] and [2000,2023]
fig, ax = plt.subplots(figsize=(10, 6))

# Filter data for Senegal and the specified years
senegal_df_1980_2000 = df[(df['Country'] == 'Senegal') & (df['Year'].dt.year.between(1980, 2000))]
senegal_df_2000_2023 = df[(df['Country'] == 'Senegal') & (df['Year'].dt.year.between(2000, 2023))]

# Plot histograms
ax.hist(senegal_df_1980_2000['Temperature'], bins=20, alpha=0.5, label='1980-2000')
ax.hist(senegal_df_2000_2023['Temperature'], bins=20, alpha=0.5, label='2000-2023')

# Customize plot
plt.title('Temperature Distribution in Senegal')
plt.xlabel('Temperature')
plt.ylabel('Frequency')
plt.legend()
plt.show()
# Plot a bar chart for average temperature per country
fig, ax = plt.subplots(figsize=(12, 8))

# Group by country and calculate the average temperature
avg_temp_by_country = df.groupby('Country')['Temperature'].mean().sort_values(ascending=False)

# Plot the bar chart
avg_temp_by_country.plot(kind='bar', ax=ax, color='skyblue')
plt.title('Average Temperature Per Country')
plt.xlabel('Country')
plt.ylabel('Average Temperature')
plt.xticks(rotation=45, ha='right')
plt.show()
