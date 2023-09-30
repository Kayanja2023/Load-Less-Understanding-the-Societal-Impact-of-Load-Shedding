import matplotlib.pyplot as plt
import pandas as pd

# Read the data from the CSV file in the specified location
df = pd.read_csv('C:\\Users\\Dell\\Downloads\\data.csv')

# Group the data by 'Institution Type' and 'Load-shedding' and count the occurrences
grouped_data = df.groupby(['Institution Type', 'Load-shedding']).size().reset_index(name='Count')

# Create a stacked bar chart
plt.figure(figsize=(12, 6))

# Initialize an empty dictionary to hold the bottom values for each stack
bottom_dict = {}

for load_shedding_level in grouped_data['Load-shedding'].unique():
    subset = grouped_data[grouped_data['Load-shedding'] == load_shedding_level]
    bottoms = [bottom_dict.get(inst_type, 0) for inst_type in subset['Institution Type']]
    plt.bar(subset['Institution Type'], subset['Count'], label=load_shedding_level, bottom=bottoms)
    
    # Update the bottom values for the next stack
    for inst_type, count in zip(subset['Institution Type'], subset['Count']):
        bottom_dict[inst_type] = bottom_dict.get(inst_type, 0) + count

# Add labels and title
plt.xlabel('Institution Type')
plt.ylabel('Count')
plt.title('Impact of Load-shedding on Different Types of Educational Institutions')
plt.legend(title='Load-shedding Level')

# Show the plot
plt.show()