import numpy as np
import matplotlib.pyplot as plt
# GLOBAL VARIABLES
COLS = 10
ROWS = 10

# functions
def make2DArray(cols, rows):
    array_2d = np.zeros((rows, cols), dtype=int)
    return array_2d

def randomFill2DArray(array):
    array[:] = np.random.choice([0, 1], size=array.shape)

def neighboors(array,row, col):
    liveNeighbors = 0
    ROWS, COLS = array.shape
    for i in range(-1, 2): #loopear para encontrar celular vecinas
        for j in range(-1, 2):
            if i == 0 and j == 0: #estas coords correspondan a la celula del medio
                continue
            if row + i < 0 or col + j < 0 or row + i >= ROWS or col + j >= COLS: #vecinos se salen de la grilla
                continue
            liveNeighbors = liveNeighbors + array[row+i][col+j]
    return liveNeighbors

def applyRule(grid):
    ROWS, COLS = grid.shape
    gridNew = np.copy(grid) #hacemos los cambios en el array nuevo
    for i in 

grid = make2DArray(COLS, ROWS) #creamos el array
randomFill2DArray(grid) #lo llenamos de 1 y 0 de forma aleatoria
print(grid)
n = neighboors(grid, 8, 9)
print(n)
#print(left, mid,right)

