import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Patch
from matplotlib.lines import Line2D

# Set the size of the grid
size_x, size_y, size_z = 20, 20, 5

# Set parameters for SEIRD model
lambda_rate = 0.02  # Exposure rate
beta = 0.2  # Infection rate
alpha = 0.1  # Recovery rate
delta = 0.05  # Mortality rate

# Initialize the grid with all susceptible individuals
initial_state = np.zeros((size_x, size_y, size_z))

# Function to update the state of the grid based on SEIRD model rules
def update(frameNum, imgs, grid, size_x, size_y, size_z):
    newGrid = grid.copy()

    for i in range(size_x):
        for j in range(size_y):
            for k in range(size_z):
                # Rule: Susceptible to Exposed
                if grid[i, j, k] == 0 and np.random.rand() < lambda_rate:
                    newGrid[i, j, k] = 1

                # Rule: Exposed to Infected
                elif grid[i, j, k] == 1 and np.random.rand() < beta:
                    newGrid[i, j, k] = 2

                # Rule: Infected to Recovered or Dead
                elif grid[i, j, k] == 2:
                    if np.random.rand() < alpha:
                        newGrid[i, j, k] = 3  # Recovered
                    elif np.random.rand() < delta:
                        newGrid[i, j, k] = 4  # Dead

    # Update data for each subplot
    for idx, img in enumerate(imgs):
        img.set_array(newGrid[:, :, idx])

    grid[:] = newGrid[:]
    return imgs

# Set up subplots for each layer
fig, axs = plt.subplots(1, size_z + 1, figsize=(size_z * 4 + 1, 4))

# Initialize subplots with the initial state
imgs = [ax.imshow(initial_state[:, :, i], cmap='viridis', vmin=0, vmax=4) for i, ax in enumerate(axs[:-1])]

# Set up the animation
ani = animation.FuncAnimation(fig, update, fargs=(imgs, initial_state, size_x, size_y, size_z),
                              frames=50, interval=200)

# Add colorbar legend
cbar_ax = fig.add_axes([0.93, 0.15, 0.02, 0.7])
cbar = fig.colorbar(imgs[0], cax=cbar_ax, ticks=[0, 1, 2, 3, 4])
cbar.set_ticklabels(['Susceptible', 'Exposed', 'Infected', 'Recovered', 'Dead'])
# Create a legend for the different states (for reference)
legend_elements = [
    Line2D([0], [0], marker='o', color='white', label='Susceptible', markerfacecolor='white', markersize=10),
    Line2D([0], [0], marker='o', color='gray', label='Exposed', markerfacecolor='gray', markersize=10),
    Line2D([0], [0], marker='o', color='orange', label='Infected', markerfacecolor='orange', markersize=10),
    Line2D([0], [0], marker='o', color='green', label='Recovered', markerfacecolor='green', markersize=10),
    Line2D([0], [0], marker='o', color='red', label='Dead', markerfacecolor='red', markersize=10)
]
# Add legend to the last subplot (for reference)
axs[-1].legend(handles=legend_elements, loc='center', bbox_to_anchor=(0.5, -0.2), ncol=5)

plt.show()

