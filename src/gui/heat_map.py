import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

df = pd.read_csv('data/combined/data_03.csv')

df['Year'] = df['Year'].astype(int)

df_statewise_dollars = df.groupby('State')['Total Storms'].sum().reset_index()

us_map = gpd.read_file("data/gui/states/cb_2018_us_state_500k.shp")

us_map = us_map.merge(df_statewise_dollars, left_on="NAME", right_on="State", how="left")

valid_states = [
    "Alabama", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", 
    "Florida", "Georgia", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", 
    "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", 
    "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", 
    "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", 
    "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", 
    "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"
]

us_map = us_map[us_map["NAME"].isin(valid_states)]

print(us_map["NAME"].unique())

us_map["Total Storms"] = pd.to_numeric(us_map["Total Storms"], errors="coerce").fillna(0)

cmap = mcolors.LinearSegmentedColormap.from_list("yellow_red", ["lightyellow", "red"])
fig, ax = plt.subplots(1, 1, figsize=(12, 8))
us_map.plot(column='Total Storms', cmap=cmap, linewidth=0.8, edgecolor='black',
            legend=True, ax=ax, missing_kwds={"color": "lightgrey", "label": "No Data"})

plt.title("Heatmap of Total Total Storms by State")
plt.axis("off")
plt.show()
