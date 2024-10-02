import pandas as pd
import matplotlib.pyplot as plt

# Read file names from list.txt
with open('list.txt', 'r') as f:
    file_list = [line.strip() for line in f.readlines()]

# Initialize a DataFrame to store coverage data for each scaffold
all_coverage_data = pd.DataFrame()

# Loop through each file and merge coverage data
for file in file_list:
    # Read each coverage file
    coverage_data = pd.read_csv(file, sep='\t', header=None, names=['scaffold', 'position', 'depth'])
    
    # Calculate the average coverage for each scaffold
    avg_coverage = coverage_data.groupby('scaffold')['depth'].mean().reset_index()
    
    # Rename the column based on the file name and merge the data
    avg_coverage.columns = ['scaffold', f'{file}_mean_depth']
    
    if all_coverage_data.empty:
        all_coverage_data = avg_coverage
    else:
        all_coverage_data = pd.merge(all_coverage_data, avg_coverage, on='scaffold', how='outer')

# Calculate the average coverage across all files for each scaffold
all_coverage_data['mean_depth_across_samples'] = all_coverage_data.iloc[:, 1:].mean(axis=1)

# Save the result to a file
all_coverage_data.to_csv('average_coverage_by_scaffold.csv', index=False)

# Plot the average coverage with scaffold on the x-axis and coverage on the y-axis
plt.figure(figsize=(20, 6))  # Set the plot size
plt.bar(all_coverage_data['scaffold'], all_coverage_data['mean_depth_across_samples'])
plt.xlabel('Scaffold')
plt.ylabel('Average Coverage')
plt.title('Average Coverage by Scaffold')
plt.xticks([])  # Skip displaying scaffold names if too many
plt.tight_layout()

# Display the plot
plt.show()

# Optionally save the plot to a file
plt.savefig('average_coverage_by_scaffold.png')
