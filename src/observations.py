import os
import pandas as pd

# Get the current directory
current_directory = os.getcwd()

# Update the file paths with the correct relative paths and the "data_files" directory
file_paths = [
    os.path.join(current_directory, "data_files", "HomeA-meter4_2016.csv")
]

# Initialize a variable to store the total number of observations
total_observations = 0

# Iterate through each file and count the number of rows
for file_path in file_paths:
    df = pd.read_csv(file_path)
    total_observations += len(df)

print("Total Observations:", total_observations)
