import matplotlib.pyplot as plt
# Data_Customer_CarType
categories = ['SUV', 'Sedan', 'Hactchback']
values = [34, 52, 14]
max_height = 100

# Create two subplots (one for each graph)
fig, axs = plt.subplots(2, 1, figsize=(6, 8))

# Plot for SUV
axs[0].bar(categories[0], values[0], color='blue', alpha=0.7)
axs[0].set_ylim([0, max_height])
axs[0].set_ylabel('Percentage')

# Plot for Sedan
axs[1].bar(categories[1], values[1], color='green', alpha=0.7)
axs[1].set_ylim([0, max_height])
axs[1].set_ylabel('Percentage')

# Plot for Hatchback
axs[1].bar(categories[1], values[1], color='pink', alpha=0.7)
axs[1].set_ylim([0, max_height])
axs[1].set_ylabel('Percentage')

# Add titles and labels
axs[0].set_title('Graph for SUV')
axs[1].set_title('Graph for Sedan')
axs[2].set_title('Graph for Hatchback')

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()
