import pandas as pd

# Read the two CSV files into Pandas DataFrames
df1 = pd.read_csv("file1.txt", header=None)  # Replace with your first file path
df2 = pd.read_csv("file2.txt", header=None)  # Replace with your second file path

# Assign the column indexes to be joined
df1_index = 0
df2_index = 2

# Join both DataFrames
# equivalent to sql = `select * from df1 inner join df2 on df1_index=df2_index`
merged_df = pd.merge(df1, df2, how='inner', left_on=df1_index, right_on=df2_index, suffixes=('_file1','_file2'))

# Get the columns to be the output
columns_to_print = merged_df.columns[2:]

# Create a new DataFrame for the output
# df = merged_df[2:]
# df = merged_df
df = merged_df[columns_to_print]

# Output
print(df.to_string(index=True, header=True))

# Write to a CSV file
# df.to_csv('output.csv', header=False, index=False)
