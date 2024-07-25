import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('G:\\Python\\supermarket_sales - Sheet1.csv')

# Preprocessing
data['Date'] = pd.to_datetime(data['Date'])
data['Month'] = data['Date'].dt.month 

# Analysis
ts = data.groupby('Product line')['Total'].sum()
avs = data.groupby('Product line')['Total'].mean()

'''

In pandas, groupby is a powerful function that is used for splitting the data into groups based on some
criteria, applying a function to each group independently, and then combining the results. It is a key 
tool for data manipulation and analysis in Python.

'''

# Visualize total and average sales by department
plt.figure(figsize=(12, 6))
'''
function is used to create a new figure or a plotting area with a specific size.
'''
plt.subplot(1, 2, 1)
ts.plot(kind='bar',color='blue')
plt.title('Total Sales by Department')
plt.xlabel('Department')
plt.ylabel('Total Sales')

plt.subplot(1, 2, 2)
avs.plot(kind='bar', color='green')
#Converting plots in bar ---kind='bar'---
plt.title('Average Sales by Department')
plt.xlabel('Department')
plt.ylabel('Average Sales')

plt.tight_layout()

'''
In Matplotlib, the .tight_layout() function is used to automatically adjust the subplot parameters to 
give specified padding between the subplots and around the figure. It helps in preventing overlapping 
of subplots, axis labels, and titles, making the plot more aesthetically pleasi
'''
plt.show()

# Analyze seasonal trends in sales by month
total_sales_by_month = data.groupby('Month')['Total'].sum()

# Visualize seasonal trends in sales
plt.figure(figsize=(10, 6))
plt.plot(total_sales_by_month, marker='o', color='purple')
plt.title('Seasonal Trends in Sales by Month')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.xticks(range(1, 13))  # Assuming data spans a year -- Sets Location in x - axsis from 1 - 12
plt.grid()
# function in Matplotlib is used to display gridlines on a plot.
plt.show()

# Investigate total sales by city and payment method
tsc = data.groupby(['City', 'Payment'])['Total'].sum().unstack()

'''
The .unstack() method in pandas is used to pivot (unstack) a level of the index labels. 
'''

# Visualize total sales by city and payment method
tsc.plot(kind='bar', stacked=True, figsize=(10, 6))
plt.title('Total Sales by City and Payment Method')
plt.xlabel('City')
plt.ylabel('Total Sales')
plt.legend(title='Payment Method')
'''
the legend function is used to add a legend to a plot to provide 
information about the data being displayed
'''
plt.show()
