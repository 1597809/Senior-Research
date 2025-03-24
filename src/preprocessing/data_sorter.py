import pandas as pd

input_file = 'data/combined/new_combined_data.csv'
output_file = 'data/combined/new_combined_data_sorted.csv'
df = pd.read_csv(input_file)

df_sorted = df.sort_values(by=['Year', 'State', 'County'])

df_sorted.to_csv(output_file, index=False)
print(f"Sorted data saved to {output_file}")
