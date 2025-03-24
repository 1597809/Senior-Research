import os
import pandas as pd

data_dir = 'data'

combined_df = pd.DataFrame()

for state_folder in os.listdir(data_dir):
    state_path = os.path.join(data_dir, state_folder)

    if not os.path.isdir(state_path):
        continue

    for csv_file in os.listdir(state_path):
        year = os.path.splitext(csv_file)[0].split()[-1]

        file_path = os.path.join(state_path, csv_file)
        df = pd.read_csv(file_path)

        if 'Name' in df.columns:
            df = df.rename(columns={'Name': 'County'})

        expected_columns = {'County', 'Total Paid Claims', 'Total Claim Dollars Paid'}
        if not expected_columns.issubset(df.columns):
            print(f"Skipping file {file_path} due to missing columns.")
            continue

        df['State/Territory'] = state_folder
        df['Year'] = int(year)

        combined_df = pd.concat([combined_df, df], ignore_index=True)

combined_df = combined_df[['State/Territory', 'Year', 'County', 'Total Paid Claims', 'Total Claim Dollars Paid']]

combined_df = combined_df.sort_values(by=['State/Territory', 'Year', 'County']).reset_index(drop=True)

combined_df.to_csv('combined_data.csv', index=False)

print("Data combined and sorted successfully into 'combined_data.csv'")
