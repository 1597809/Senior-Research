import pandas as pd
import os
from tqdm import tqdm

storm_events_dir = "data/01 Weather Data"

event_types = [
    'Thunderstorm Wind', 'Hail', 'Flash Flood', 'High Wind', 'Winter Storm', 
    'Winter Weather', 'Drought', 'Heavy Snow', 'Flood', 'Tornado', 
    'Marine Thunderstorm Wind', 'Heavy Rain', 'Heat', 'Strong Wind', 
    'Lightning', 'Excessive Heat', 'Cold/Wind Chill', 'Blizzard', 
    'Dense Fog', 'Extreme Cold/Wind Chill', 'Frost/Freeze', 'Ice Storm', 
    'High Surf', 'Funnel Cloud', 'Wildfire', 'Tropical Storm', 'Waterspout', 
    'Coastal Flood', 'Lake-Effect Snow', 'Debris Flow', 'Hurricane (Typhoon)', 
    'Rip Current', 'Dust Storm', 'Storm Surge/Tide', 'Sleet', 'Marine High Wind', 
    'Marine Hail', 'Avalanche', 'Astronomical Low Tide', 'Tropical Depression', 
    'Marine Tropical Storm', 'Freezing Fog', 'Lakeshore Flood', 'Hurricane', 
    'Dust Devil', 'Marine Strong Wind', 'Dense Smoke', 'Marine Hurricane/Typhoon', 
    'Volcanic Ashfall', 'Seiche', 'Volcanic Ash', 'Tsunami', 'Sneakerwave', 
    'Marine Tropical Depression', 'Marine Dense Fog', 'Northern Lights', 'Marine Lightning'
]

combined_data_path = "data/combined_data.csv"
combined_df = pd.read_csv(combined_data_path)

year_to_process = 2023

storm_file = os.path.join(storm_events_dir, f"Storm Events {year_to_process}.csv")

if os.path.exists(storm_file):
    print(f"Processing year: {year_to_process}")
    
    storm_data = pd.read_csv(storm_file)
    
    for index, row in tqdm(storm_data.iterrows(), total=storm_data.shape[0], desc=f"Year {year_to_process} Progress"):
        state = row['STATE']
        event_type = row['EVENT_TYPE']
        county = row['CZ_NAME']
        
        if pd.isnull(state) or state == "":
            continue
        
        if pd.isnull(county) or county == "":
            continue
        
        matched_rows = combined_df[(combined_df['State/Territory'] == state.title()) & (combined_df['County'] == county.title()) & (combined_df['Year'] == year_to_process)]
        
        if not matched_rows.empty and event_type in event_types:
            event_column = event_type
            combined_df.loc[matched_rows.index, event_column] += 1

    combined_df.to_csv(combined_data_path, index=False)
    print(f"Data for year {year_to_process} updated successfully!")

else:
    print(f"File for year {year_to_process} not found.")