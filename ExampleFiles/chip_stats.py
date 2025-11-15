# using matplotlib with numpy
# Creating data showing Popular chips bought each year
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import numpy as np
import pandas as pd

stats = {'Year': [2020, 2021, 2022],
		 'Sales': [80, 245, 280]}
df = pd.DataFrame(stats)
average_sales = np.mean(df['Sales'])

# converts float to show integers for cleaner readability
fig, ax = plt.subplots()
ax.xaxis.set_major_locator(MaxNLocator(integer=True))
plt.xlim(2019, 2023)
plt.ylim(0, 300)

# shows visual bar chart of popular chips bought per year and total sales
# also has a legend for corresponding chips and their respective colors
bar = ax.bar( df['Year'], df['Sales'], color=['#e64553', '#df8e1d', '#179299'])
plt.xlabel('Sales of Chips per Year')
plt.ylabel('Total Sales of Chips')
plt.title('Popular Chips Bought Per Year')
plt.legend(bar, ['Cheetos', 'Cool Ranch', 'Lays'], loc='upper right')
plt.show()