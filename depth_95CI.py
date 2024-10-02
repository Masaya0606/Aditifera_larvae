import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Read file names from list.txt
with open('list.txt', 'r') as f:
    file_list = [line.strip() for line in f.readlines()]  # Get file names from each line

# Read and combine coverage data from all files
all_coverage_values = []

for file in file_list:
    # Read coverage data (the third column contains coverage)
    coverage_data = pd.read_csv(file, sep='\t', header=None)

    # Extract coverage values (third column) and add to the list
    all_coverage_values.extend(coverage_data[2].tolist())

# Convert the list to a NumPy array
all_coverage_values = np.array(all_coverage_values)

# Calculate the mean and standard error
mean_coverage = np.mean(all_coverage_values)
stderr_coverage = stats.sem(all_coverage_values)

# Calculate the 95% confidence interval
confidence_interval = stats.t.interval(0.95, len(all_coverage_values)-1, loc=mean_coverage, scale=stderr_coverage)

# Display the results
print(f"Mean Coverage: {mean_coverage}")
print(f"95% Confidence Interval: {confidence_interval}")
