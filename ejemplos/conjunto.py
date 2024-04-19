import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
categories = ['A', 'B', 'C', 'D']
values = [20, 35, 30, 25]
data = np.random.normal(loc=0, scale=1, size=1000)
x_scatter = np.random.normal(loc=0, scale=1, size=100)
y_scatter = np.random.normal(loc=0, scale=1, size=100)
sizes = [30, 20, 25, 15, 10]
labels = ['A', 'B', 'C', 'D', 'E']

# Creating subplots
fig, axs = plt.subplots(2, 3, figsize=(15, 10))

# Line Plot
axs[0, 0].plot(x, y1, label='sin(x)', color='blue')
axs[0, 0].plot(x, y2, label='cos(x)', color='red')
axs[0, 0].set_title('Line Plot')
axs[0, 0].legend()

# Bar Plot
axs[0, 1].bar(categories, values, color='green')
axs[0, 1].set_title('Bar Plot')

# Histogram
axs[0, 2].hist(data, bins=30, edgecolor='black', color='purple')
axs[0, 2].set_title('Histogram')

# Scatter Plot
axs[1, 0].scatter(x_scatter, y_scatter, color='orange', s=10)
axs[1, 0].set_title('Scatter Plot')

# Pie Chart
axs[1, 1].pie(sizes, labels=labels, autopct='%1.1f%%')
axs[1, 1].set_title('Pie Chart')

# Box Plot
axs[1, 2].boxplot(data)
axs[1, 2].set_title('Box Plot')

# Adjust layout
plt.tight_layout()

# Show the combined plot
plt.show()
