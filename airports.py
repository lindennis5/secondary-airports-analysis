#for plots included 

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Figure 1: Total Flights per Secondary Canadian Airport ---
data1 = {
    'Airport': ['YYC','YEG','YWG','YOW','YHZ','YZF','YRT','YQB','YZV'],
    'Route_Frequency': [166,109,76,71,66,60,50,49,42]}
df1 = pd.DataFrame(data1)
df1 = df1.sort_values('Route_Frequency', ascending=False)
plt.figure(figsize=(12,6))
sns.set_style("whitegrid")
sns.barplot(x='Route_Frequency', y='Airport', data=df1, palette='viridis')
plt.xlabel('Total Routes')
plt.ylabel('')
plt.title('Total Flights per Secondary Canadian Airport')
for index, row in df1.iterrows():
    plt.text(row['Route_Frequency'] + 1, index, int(row['Route_Frequency']), va='center')
plt.tight_layout()
plt.show()


#Figure 2: International Flight Volume per Secondary Airport ---
data2 = {
    'Airport': ['YYC','YEG','YHZ','YOW','YQB','YWG'],
    'Total_Intl_Routes': [82,28,20,19,7,6],
    'Unique_Destinations': [27,18,13,10,5,5]}
df2 = pd.DataFrame(data2)
df2 = df2.sort_values('Total_Intl_Routes', ascending=False)
plt.figure(figsize=(10,6))
sns.barplot(x='Total_Intl_Routes', y='Airport', data=df2, palette='magma')
plt.xlabel('Total International Routes')
plt.ylabel('')
plt.title('International Flight Volume per Secondary Canadian Airport')
for index, row in df2.iterrows():
    plt.text(row['Total_Intl_Routes'] + 0.5, index,
             f"{row['Total_Intl_Routes']} routes, {row['Unique_Destinations']} destinations",
             va='center', fontsize=9)
plt.tight_layout()
plt.show()
