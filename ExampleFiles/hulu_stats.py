# Small project showing Hulu's Subscriber gain as of Sep. 2025
# We're going to put into practice of pandas, numpy and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# creating arrays for different tiers and sub counts
dataSet = {'Tier': ['Hulu SVOD-Only (On-Demand)', 'Hulu + Live TV', 'Total Hulu Subscribers'],
		   'Gain': [8.5, 100.000, 8.6],
		   'Final Total': [59.7, 4.4, 64.1]}

# storing dataSet into a pandas DataFrame
df = pd.DataFrame(dataSet)

# plotting the bar chart with custom colors and labels
df.plot(x='Tier', y=['Gain', 'Final Total'], kind='bar', figsize=(15, 10), color=['#a6d189', '#81c8be'])
plt.title('Hulu Subscriber Gain and Total Subscribers')
plt.xlabel('Subscription Tier')
plt.xticks(rotation=15)
plt.ylabel('Subscriber Count')
plt.ylim(0, 100)
plt.legend(['Gain', 'Total Subscribers'])
plt.show()


