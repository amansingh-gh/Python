import matplotlib.pyplot as plt

# Sample Data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
sales = [100, 120, 90, 150, 200]

# Create Line Plot
plt.plot(months, sales, color='blue', marker='o', linestyle='-')
plt.title('Monthly Sales')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(True)

# Show the graph
plt.show()
