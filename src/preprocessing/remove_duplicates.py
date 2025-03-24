import pandas as pd

df = pd.read_csv('data/combined/data_03.csv')

df_cleaned = df.drop_duplicates(subset=['Year', 'State', 'County'])

df_cleaned.to_csv('data/combined/data_031.csv', index=False)