import numpy as np
import pandas as pd

# Load the dataset
a = pd.read_csv('dataset-netflix1')

# Display basic information about the dataset
print("Dataset Information:")
print(a.info())

# Handling missing values
# Replace missing values with the mean of each column
a.fillna(a.mean(), inplace=True)

# Save the cleaned dataset to a new CSV file
a.to_csv('cleaned_dataset.csv', index=False)
print("Cleaned dataset saved successfully.")
