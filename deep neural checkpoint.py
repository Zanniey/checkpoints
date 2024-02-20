# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 16:31:09 2024

@author: User
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
# Load the dataset
df = pd.read_csv('bank.csv')

# Display basic information about the dataset
print(df.info())

# Display summary statistics
print(df.describe())
# Check for missing values
print(df.isnull().sum())

# Drop rows with missing values or impute them

# Handle categorical variables if needed
# Visualize the distribution of the target variable
df['deposit'].value_counts().plot(kind='bar')
plt.title('Distribution of Deposit (Target Variable)')
plt.show()

# Visualize relationships between features and the target variable using plots or graphs
# Convert categorical variables to numerical using Label Encoding or One-Hot Encoding
label_encoder = LabelEncoder()
df['deposit'] = label_encoder.fit_transform(df['deposit'])

# Split the dataset into features and target variable
X = df.drop('deposit', axis=1)
y = df['deposit']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
# Define the model
model = Sequential()
model.add(Dense(64, input_dim=X_train.shape[1], activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_split=0.2, verbose=1)

# Evaluate the model on the test set
_, accuracy = model.evaluate(X_test, y_test)
print('Model Accuracy: %.2f%%' % (accuracy * 100))
