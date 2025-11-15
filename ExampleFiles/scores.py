# Example code is by dataquest and posted on medium.com
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Create a sample dataset
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, np.nan],  # One missing value
    'Score': [65, 88, 95, 79]
}
# Load the data into a pandas DataFrame
df = pd.DataFrame(data)
# Clean the dataset: fill missing age with the average age
df['Age'] = df['Age'].fillna(df['Age'].mean())
# Calculate the average score using NumPy
average_score = np.mean(df['Score'])
# Output the cleaned dataset and the average score
print("Cleaned Dataset:")
print(df)
print("\nAverage Score:", average_score)

# Nice colors for each bar
colors = ['#f4b8e4', '#e5c890', '#8caaee', '#81c8be']

plt.figure(figsize=(7, 4.5))

# Bar chart of Score by Name
plt.bar(df['Name'], df['Score'], color=colors)
plt.xlabel('Name of Student', labelpad=10)
plt.ylabel('Score')
plt.title('Test Scores')

# Add Age as text labels above each bar
for x, y, age in zip(df['Name'], df['Score'], df['Age']):
    # y + 1 gives a small gap above the bar; adjust if needed
    plt.text(x, y + 1, f"Age: {age:.0f}", ha='center', va='bottom', fontsize=9)

# Average score line with label
avg = df['Score'].mean()
plt.axhline(avg, color='#e78284', linestyle='--', label=f'Average Score ({avg:.1f})')
plt.legend(loc='upper right')

# Prevent labels from getting clipped
plt.tight_layout()
plt.show()