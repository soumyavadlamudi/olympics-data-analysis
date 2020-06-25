# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file is stored in the variable path

#Code starts here

# Data Loading 
data = pd.read_csv(path)
data.rename(columns = {'Total': 'Total_Medals'}, inplace = True)
print(data.head())
# Summer or Winter
data['Better_Event'] = np.where(data['Total_Winter'].eq(data['Total_Summer']), 'Both', np.where(data['Total_Winter'] > data['Total_Summer'], 'Winter', 'Summer'))

better_event = data['Better_Event'].value_counts().idxmax()
print(better_event)

# Top 10
top_countries = pd.DataFrame(data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']])
top_countries.drop(top_countries.index[len(top_countries) - 1] , inplace = True)
def top_ten(df, col):
    country_list = []
    top_ten = df.nlargest(10, col)
    country_list = list(top_ten['Country_Name'])
    return country_list

top_10_summer = top_ten(top_countries, 'Total_Summer')
top_10_winter = top_ten(top_countries, 'Total_Winter')
top_10 = top_ten(top_countries, 'Total_Medals')
common = list(set(top_10_summer) & set(top_10_winter) & set(top_10))

# Plotting top 10
summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]
# Top Performing Countries

fig, (ax_1,ax_2,ax_3) = plt.subplots(3,1, figsize=(20,15))

plt.title('Medals won by top ten countries in summer')
plt.xlabel('Country_Name')
plt.ylabel('Total Medals Won')
ax_1.bar(summer_df['Country_Name'], summer_df['Total_Summer'])

plt.title('Medals won by top ten countries in Winter')
plt.xlabel('Country_Name')
plt.ylabel('Total Medals Won')
ax_2.bar(winter_df['Country_Name'], winter_df['Total_Winter'])

plt.title('Medals won by top ten countries irrespective of weather')
plt.xlabel('Country_Name')
plt.ylabel('Total Medals Won')
ax_3.bar(top_df['Country_Name'], top_df['Total_Medals'])

max_data = []
summer_df['Golden_Ratio'] = summer_df['Gold_Summer']/summer_df['Total_Summer']
summer_max_ratio_index = summer_df['Golden_Ratio'].idxmax()
summer_country_gold = summer_df['Country_Name'][summer_max_ratio_index]
summer_max_ratio = summer_df['Golden_Ratio'][summer_max_ratio_index]
summer_max_ratio = max(summer_df['Golden_Ratio'])
summer_country_gold = summer_df.loc[summer_df['Golden_Ratio'].idxmax(), ['Country_Name']]
summer_country_gold = summer_country_gold['Country_Name']

# summer_df['Golden_Ratio']=summer_df['Gold_Summer']/summer_df['Total_Summer'] 
# summer_max_ratio=max(summer_df['Golden_Ratio']) 
# summer_country_gold=summer_df.loc[summer_df['Golden_Ratio'].idxmax(),'Country_Name']

winter_df['Golden_Ratio'] = winter_df['Gold_Winter']/winter_df['Total_Winter']
winter_country_gold = winter_df.loc[winter_df['Golden_Ratio'].idxmax(), ['Country_Name']]
winter_max_ratio = max(winter_df['Golden_Ratio'])
winter_country_gold = winter_country_gold['Country_Name']

top_df['Golden_Ratio'] = top_df['Gold_Total']/top_df['Total_Medals']
top_max_ratio_index = top_df['Golden_Ratio'].idxmax()
top_country_gold = top_df.loc[top_max_ratio_index, ['Country_Name']]
top_max_ratio = top_df['Golden_Ratio'][top_max_ratio_index]
top_country_gold = top_country_gold['Country_Name']

most_points = max(top_max_ratio, winter_max_ratio, summer_max_ratio)
print(most_points)
best_country = summer_country_gold
# Best in the world 
data_1 = data[:-1]
data_1['Total_Points'] = data_1['Gold_Total'] * 3 + data_1['Silver_Total'] * 2 + data_1['Bronze_Total']

most_points = max(data_1['Total_Points'])
best_country = data_1.loc[data_1['Total_Points'].idxmax(), ['Country_Name']]

best_country = best_country['Country_Name']
best = data[data['Country_Name'] == best_country]
best = best[['Gold_Total','Silver_Total','Bronze_Total']]
best.plot.bar(stacked = True)
plt.xlabel('United_States')
plt.ylabel('Medals Tally')
plt.xticks(rotation = 45)




# Plotting the bestplt.bar(winter_df['Country_Name'], winter_df['Total_Summer'], ax = ax_2)
# ax_2.title("Medals won by top ten countriesin Winter")
# plt.bar(top_df['Country_Name'], top_df['Total_Summer'], ax = ax_3)
# ax_3.title("Medals won by top ten countries irrespectve of weather")
# plt.show()




