import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/combined/data_03.csv')

df_statewise_dollars = df.groupby('State')['Claims Paid'].sum()

plt.figure(figsize=(12, 8))
df_statewise_dollars.plot(kind='bar')
plt.title('Claims Paid by State')
plt.ylabel('Claims Paid')
plt.xlabel('State')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()