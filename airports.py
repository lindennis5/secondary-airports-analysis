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

#Figure 3: Flights to geographical destinations
import matplotlib.pyplot as plt

airports = ['YYC', 'YEG', 'YHZ', 'YOW', 'YQB', 'YWG']
total_routes = [82, 28, 20, 19, 7, 6]
unique_destinations = [27, 18, 13, 10, 5, 5]
airlines = [
    'AC, WS, AA, UA, DL, TS',
    'UA, AC, WS',
    'WS, AC, UA',
    'AC, UA, AA, LH',
    'TS, UA',
    'UA, AC, WS']
fig, ax = plt.subplots(figsize=(10, 4))
ax.axis('tight')
ax.axis('off')

table_data = []
for i in range(len(airports)):
    table_data.append([airports[i], total_routes[i], unique_destinations[i], airlines[i]])

table = ax.table(cellText=table_data,
                 colLabels=['Airport', 'Total Intl Routes', 'Unique Destinations', 'Most Frequent Airline(s)'],
                 cellLoc='center',
                 loc='center')

table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1, 2)  # scale width, height

plt.title('Intl Flight Volume per Secondary Airport in Canada', fontsize=12, pad=12)
plt.tight_layout()
plt.savefig('secondary_airports_table.png', dpi=300)
plt.show()


import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Airport': ['YEG', 'YHZ', 'YOW', 'YQB', 'YWG', 'YYC'],
    'USA': [13, 9, 8, 4, 4, 15],
    'Mexico/Caribbean': [2, 4, 0, 2, 0, 4],
    'Europe': [2, 3, 4, 1, 0, 9],
    'Asia': [0, 0, 0, 0, 0, 2],
    'Other': [0, 1, 0, 0, 0, 0]}

df = pd.DataFrame(data)
df.set_index('Airport', inplace=True)

# Plot
ax = df.plot(kind='bar', stacked=True, figsize=(12,6), colormap='tab20c')

plt.title('International Flight Distribution by Region from Secondary Canadian Airports')
plt.ylabel('Number of International Routes')
plt.xlabel('Airport')
plt.xticks(rotation=0)
plt.legend(title='Region')
plt.tight_layout()
plt.show()

#Figure 4: focus of flights
import matplotlib.pyplot as plt

airports = ['YYC (Calgary)', 'YEG (Edmonton)', 'YHZ (Halifax)', 'YOW (Ottawa)',
            'YQB (Quebec City)', 'YWG (Winnipeg)']
focus =
['Mixed business, tourism, transatlantic',
    'Mostly U.S. business & leisure',
    'Tourism-heavy; seasonal Europe & Caribbean',
    'Government/business; Europe & U.S. East Coast',
    'Tourism-oriented; Caribbean & Europe',
    'U.S. Midwest connections; some leisure travel']

fig, ax = plt.subplots(figsize=(12,3))
ax.axis('tight')
ax.axis('off')

table_data = list(zip(airports, focus))
table = ax.table(cellText=table_data, colLabels=["Airport", "Primary Focus of International Flights"],
                 cellLoc='left', loc='center', colColours=['lightblue','lightgreen'])

table.auto_set_font_size(False)
table.set_fontsize(10)
table.auto_set_column_width([0,1])

plt.tight_layout()
plt.savefig('airport_focus_table.png', dpi=300)
plt.show()

#Figure 5: Codes Reference
import matplotlib.pyplot as plt

types = ['Airport']*11 + ['Airline']*7
codes = ['YYC','YEG','YWG','YOW','YHZ','YZF','YNT','YRT','YQB','YZV','AC','WS','AA','UA','DL','TS','LH']
names = [
    'Calgary International Airport','Edmonton International Airport','Winnipeg James Armstrong Richardson International Airport',
    'Ottawa Macdonald–Cartier International Airport','Halifax Stanfield International Airport','Yellowknife Airport',
    'Gatineau–Ottawa Executive Airport','Rankin Inlet Airport','Québec City Jean Lesage International Airport',
    'Sept-Îles Airport','Air Canada','WestJet','American Airlines','United Airlines','Delta Air Lines','Air Transat','Lufthansa'
]
locations = [
    'Calgary, Alberta, Canada','Edmonton, Alberta, Canada','Winnipeg, Manitoba, Canada','Ottawa, Ontario, Canada',
    'Halifax, Nova Scotia, Canada','Yellowknife, Northwest Territories, Canada','Gatineau, Quebec, Canada',
    'Rankin Inlet, Nunavut, Canada','Québec City, Quebec, Canada','Sept-Îles, Quebec, Canada',
    'Canada','Canada','United States','United States','United States','Canada','Germany'
]

fig, ax = plt.subplots(figsize=(14,4))
ax.axis('tight')
ax.axis('off')

table_data = list(zip(types, codes, names, locations))
table = ax.table(cellText=table_data,
                 colLabels=["Type","Code","Name","City / Province / Country"],
                 cellLoc='left', loc='center',
                 colColours=['lightgrey','lightblue','lightgreen','lightyellow'])

table.auto_set_font_size(False)
table.set_fontsize(10)
table.auto_set_column_width([0,1,2,3])

plt.tight_layout()
plt.savefig('airport_airline_reference.png', dpi=300)
plt.show()

