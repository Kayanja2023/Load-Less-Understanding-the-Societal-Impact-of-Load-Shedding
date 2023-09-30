import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Input from the data source in a data frame 
df = pd.read_csv('C:\\Users\\Dell\\Downloads\\data.csv')

# Grouped the data by 'Institution Type' and 'Load-shedding' and count the occurrences
grouped_data = df.groupby(['Institution Type', 'Load-shedding']).size().reset_index(name='Count')

# Created a pivot table for the heatmap
pivot_table = pd.pivot_table(grouped_data, values='Count', index=['Institution Type'], columns=['Load-shedding'], fill_value=0)

# Create the heatmap
plt.figure(figsize=(12, 6))
sns.heatmap(pivot_table, annot=True, cmap="YlGnBu", fmt="d")

# Added labels and title
plt.xlabel('Load-shedding Impact')
plt.ylabel('Institution Type')
plt.title('Impact of Load-shedding on Different Types of Educational Institutions')

# Show the plot
plt.show()
