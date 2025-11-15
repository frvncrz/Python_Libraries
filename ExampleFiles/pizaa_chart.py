import matplotlib.pyplot as plt
import pandas as pd

data = {'Pizza': ['Dominoes', 'Papa Johns', 'Pizza Hut'],
		'Sales': [2500, 4300, 2500]}
df = pd.DataFrame(data)

plt.bar(df['Pizza'], df['Sales'], color=['#8caaee', '#babbf1', '#838ba7'])
plt.xlabel('Pizza Places')
plt.ylabel('Pizza Sales')
plt.title('Pizza Chart')
plt.ylim(0, 15000)
plt.show()