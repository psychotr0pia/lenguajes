import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Patch
from matplotlib.lines import Line2D
from CAListener import CAListener

class CAVariables:
    def __init__(self, size_x, size_y, size_z, lambda_rate, beta, alpha, delta):
        self.size_x = size_x
        self.size_y = size_y
        self.size_z = size_z
        self.lambda_rate = lambda_rate
        self.beta = beta
        self.alpha = alpha
        self.delta = delta

class CellularAutomata:
    def __init__(self, variables):
        self.variables = variables
        self.initial_state = np.random.choice([0, 1], size=(self.variables.size_x, self.variables.size_y, self.variables.size_z))

    def update(self, frameNum, imgs, grid):
        newGrid = grid.copy()

        for i in range(self.variables.size_x):
            for j in range(self.variables.size_y):
                for k in range(self.variables.size_z):
                    # Rule: Susceptible to Exposed
                    if grid[i, j, k] == 0 and np.random.rand() < self.variables.lambda_rate:
                        newGrid[i, j, k] = 1

                    # Rule: Exposed to Infected
                    elif grid[i, j, k] == 1 and np.random.rand() < self.variables.beta:
                        newGrid[i, j, k] = 2

                    # Rule: Infected to Recovered or Dead
                    elif grid[i, j, k] == 2:
                        if np.random.rand() < self.variables.alpha:
                            newGrid[i, j, k] = 3  # Recovered
                        elif np.random.rand() < self.variables.delta:
                            newGrid[i, j, k] = 4  # Dead

        # Update data for each subplot
        for idx, img in enumerate(imgs):
            img.set_array(newGrid[:, :, idx])
        grid[:] = newGrid[:]
        return imgs

    def run_simulation(self):
        fig, axs = plt.subplots(1, self.variables.size_z, figsize=(self.variables.size_z * 4, 4))
        imgs = [ax.imshow(self.initial_state[:, :, i], cmap='viridis', vmin=0, vmax=4) for i, ax in enumerate(axs)]

        ani = animation.FuncAnimation(fig, self.update, fargs=(imgs, self.initial_state),
                                      frames=10, interval=500, save_count=50)

        # Add colorbar legend
        cbar_ax = fig.add_axes([0.93, 0.15, 0.02, 0.7])
        cbar = fig.colorbar(imgs[0], cax=cbar_ax, ticks=[0, 1, 2, 3, 4])
        cbar.set_ticklabels(['Susceptible', 'Exposed', 'Infected', 'Recovered', 'Dead'])

        # Create a legend for the different states (for reference7=)
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

if __name__ == '__main__':
    # Create an instance of CAVariables with desired parameters
    ca_variables = CAVariables(size_x=20, size_y=20, size_z=3, lambda_rate=0.1, beta=0.2, alpha=0.3, delta=0.4)

    # Create an instance of CellularAutomata with the CAVariables instance
    ca_instance = CellularAutomata(variables=ca_variables)

    # Run the simulation
    ca_instance.run_simulation()
