import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/combined/data_03.csv')

storm_types = ['Dust', 'Flood', 'Hail', 'Hurricane', 'Heavy Rain', 'Snow', 'Thunderstorm', 'Tornado', 'Wildfire', 'Wind']

df_storm_means = df[storm_types].mean().sort_values(ascending=False)

plt.figure(figsize=(12, 8))
df_storm_means.plot(kind='bar')
plt.title('Average Storm Type Frequencies Across All States')
plt.ylabel('Average Number of Storms')
plt.xlabel('Storm Type')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
