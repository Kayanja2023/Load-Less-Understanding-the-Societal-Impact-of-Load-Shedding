import matplotlib.pyplot as plt
import pandas as pd

# Read the data from the CSV file in the specified location
df = pd.read_csv('C:\\Users\\Dell\\Downloads\\data.csv')

# Group the data by 'Age' and 'Load-shedding' and count the occurrences
grouped_data = df.groupby(['Age', 'Load-shedding']).size().reset_index(name='Count')

# Create a bar chart
plt.figure(figsize=(12, 6))
for age_group in grouped_data['Age'].unique():
    subset = grouped_data[grouped_data['Age'] == age_group]
    plt.bar(subset['Load-shedding'], subset['Count'], label=age_group)

# Add labels and title
plt.xlabel('Load-shedding Impact')
plt.ylabel('Count')
plt.title('Impact of Load-shedding on Different Age Groups')
plt.legend(title='Age Groups')

# Show the plot
plt.show()
