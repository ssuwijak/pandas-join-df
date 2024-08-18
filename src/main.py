import pandas as pd

# Read the two CSV files into Pandas DataFrames
df1 = pd.read_csv("file1.txt", header=None)  # Replace with your first file path
df2 = pd.read_csv("file2.txt", header=None)  # Replace with your second file path

# Assign custom column names (replace with appropriate names)
df1_index = 0
df2_index = 2

# Assuming the ID column is named 'id' in both files
merged_df = pd.merge(df1, df2, how='inner', left_on=df1_index, right_on=df2_index, suffixes=('_file1','_file2'))

# Get columns to be output
columns_to_print = merged_df.columns[2:]

# df = merged_df[2:]
# df = merged_df
df = merged_df[columns_to_print]

print(df.to_string(index=True, header=True))

# Write to a CSV file
# df.to_csv('output.csv', header=False, index=False)