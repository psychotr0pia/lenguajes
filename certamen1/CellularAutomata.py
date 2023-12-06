import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Patch
from matplotlib.lines import Line2D
from antlr4 import *
from CALexer import CALexer
from CAParser import CAParser
from CAListener import CAListener

class CustomListener(CAListener):
    def __init__(self):
        self.CAVariables = CAVariables()

    def exitVariable(self, ctx):
        variable_name = ctx.getChild(0).getText()
        variable_value = float(ctx.getChild(2).getText())

        if variable_name == 'X':
            self.CAVariables.size_x = int(variable_value)
        elif variable_name == 'Y':
            self.CAVariables.size_y = int(variable_value)
        elif variable_name == 'Z':
            self.CAVariables.size_z = int(variable_value)
        elif variable_name == 'LAMBDA':
            self.CAVariables.lambda_rate = variable_value
        elif variable_name == 'BETA':
            self.CAVariables.beta = variable_value
        elif variable_name == 'ALPHA':
            self.CAVariables.alpha = variable_value
        elif variable_name == 'DELTA':
            self.CAVariables.delta = variable_value
        elif variable_name == 'INFECTADOS':
            self.CAVariables.initial_infected = int(variable_value)

class CAVariables:
    def __init__(self, size_x=100, size_y=100, size_z=5, 
                 lambda_rate=0.8, beta=0.8, 
                 alpha=0.3, delta=0.01, 
                 initial_infected=10): #como en el pague inc: mucha contagio y poca mortalidad 
        self.size_x = size_x
        self.size_y = size_y
        self.size_z = size_z
        self.lambda_rate = lambda_rate
        self.beta = beta
        self.alpha = alpha
        self.delta = delta
        self.initial_infected = initial_infected

class CellularAutomata:
    def __init__(self, variables):
        self.variables = variables
        self.initial_state = self.initialize_grid()
    def initialize_grid(self):
        initial_state = np.zeros((self.variables.size_x, self.variables.size_y, self.variables.size_z))

        # Infect a set number of people
        infected_count = 0
        while infected_count < self.variables.initial_infected:
            i_rand, j_rand, k_rand = np.random.randint(0, self.variables.size_x), np.random.randint(0, self.variables.size_y), np.random.randint(0, self.variables.size_z)
            if initial_state[i_rand, j_rand, k_rand] == 0:
                initial_state[i_rand, j_rand, k_rand] = 2  # Infected
                infected_count += 1

        return initial_state
    
    def count_infected_neighbors(self, grid, i, j, k):
        count = 0
        for di in range(-1, 2):
            for dj in range(-1, 2):
                for dk in range(-1, 2):
                    if di == dj == 0:  # Skip the current cell
                        continue
                    ni, nj, nk = i + di, j + dj, k + dk
                    if 0 <= ni < self.variables.size_x and 0 <= nj < self.variables.size_y and 0 <= nk < self.variables.size_z:
                        if grid[ni, nj, nk] == 2:  # Infected cell
                            count += 1
        return count

    def update(self, frameNum, imgs, grid):
        newGrid = grid.copy()

        for i in range(self.variables.size_x):
            for j in range(self.variables.size_y):
                for k in range(self.variables.size_z):
                    # Rule: Susceptible to Exposed
                    infected_neighbors = self.count_infected_neighbors(grid, i, j, k)
                    if grid[i, j, k] == 0 and np.random.rand() < self.variables.lambda_rate and infected_neighbors > 0:
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
    # Create an instance of CAVariables 
    # with default parameters
    ca_variables = CAVariables()

    # Create an instance of CellularAutomata 
    # with the CAVariables instance
    ca_instance = CellularAutomata(variables=ca_variables)

    # Read the input from the user or from a file
    input_str = input("Enter the configuration: ")

    # Create the lexer, parser, and walker
    lexer = CALexer(InputStream(input_str))
    stream = CommonTokenStream(lexer)
    parser = CAParser(stream)
    
    # Attach the custom listener to the parser
    custom_listener = CustomListener()
    parser.addParseListener(custom_listener)

    # Start the parsing
    tree = parser.start()

    # Access the CAVariables from the listener
    ca_variables = custom_listener.CAVariables

    # Now you have the modified CAVariables, 
    # you can use it in your CellularAutomata instance
    ca_instance = CellularAutomata(variables=ca_variables)

    # Run the simulation
    ca_instance.run_simulation()