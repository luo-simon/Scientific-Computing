"""
Project 4 - Game of Life
Game of life is a cellular automaton devised by John Conway in 70's
https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

The game consists of two dimensional orthogonal grid of cells.
Cells are in two possible states, alive or dead.
Each cell interacts with its eight neighbours; each time step the following transitions occur:
    - Any live cell with fewer than two live neighbours dies, as if caused by underpopulation
    - Any live cell with more than three live neighbours dies, as if by overcrowding
    - Any live cell with two or three live neighbours lives on to the next generation
    - Any dead cell with exactly three live neighbours becomes a live cell

The initial pattern constitutes the seed, and the system is left to evolve according to rules.
Deaths and births happen simultaneously. Implement the Game of Life using Numpy.
Try first a 32x32 square grid and for example a crossshaped initial pattern
Try also other grids and initial patterns (e.g. random pattern). Try to avoid for loops.

For visualization you can use Matplotlib
"""
import matplotlib.pyplot as plt
import numpy as np

TIME_STEP = 1/60
GRID_SIZE = 80
INITIAL_SEED = 4 # 0: Random, 1: Cross-shape, 2: Pulsar, 3: Square block, 4: Glider Gun Generator!

def main():
    if INITIAL_SEED == 0:
        grid = np.random.randint(0,2, size=(GRID_SIZE,GRID_SIZE), dtype=bool)
    else:
        if INITIAL_SEED == 1:
            shape = ("010\n111\n010")
        elif INITIAL_SEED == 2:
            shape = ("000010000010000\n000010000010000\n000011000110000\n\n111001101100111\n001010101010100\n000011000110000\n\n"
                    "000011000110000\n001010101010100\n111001101100111\n\n000011000110000\n000010000010000\n000010000010000")
        elif INITIAL_SEED == 3:
            shape = ("11111111\n11111111\n11111111\n11111111\n11111111\n11111111\n11111111\n11111111")
        elif INITIAL_SEED == 4:
            shape = ("00000000000000000000000001000000000000\n"
                     "00000000000000000000000101000000000000\n"
                     "00000000000001100000011000000000000110\n"
                     "00000000000010001000011000000000000110\n"
                     "01100000000100000100011000000000000000\n"
                     "01100000000100010110000101000000000000\n"
                     "00000000000100000100000001000000000000\n"
                     "00000000000010001000000000000000000000\n"
                     "00000000000001100000000000000000000000\n")     
        grid = generate_grid(shape)

    grid_next = np.zeros(shape=(GRID_SIZE, GRID_SIZE), dtype=bool)

    while True:
        plt.imshow(grid)
        plt.draw()

        for y in range(GRID_SIZE):
            for x in range(GRID_SIZE):
                if not (1 < y < GRID_SIZE-1) or not (0 < x < GRID_SIZE-1):
                    continue
                n = 0 # Number of live neighbours
                n += grid[y-1][x-1]; n += grid[y-1][ x ]; n += grid[y-1][x+1]
                n += grid[ y ][x-1]; n += grid[ y ][x+1]
                n += grid[y+1][x-1]; n += grid[y+1][ x ]; n += grid[y+1][x+1]

                if grid[y][x] == 1:
                    if n < 2 or n > 3:
                        grid_next[y][x] = 0
                    else:
                        grid_next[y][x] = 1
                else:
                    if n == 3:
                        grid_next[y][x] = 1
               
        grid = grid_next
        grid_next = np.zeros(shape=(GRID_SIZE, GRID_SIZE), dtype=bool)
        plt.pause(TIME_STEP)
        plt.clf()

def generate_grid(shape):
    grid = np.zeros(shape=(GRID_SIZE, GRID_SIZE), dtype=bool)
    lines = [[int(char) for char in x] for x in shape.splitlines()]

    h = len(lines)
    w = len(lines[0])

    for i in range(h):
        if (len(lines[i]) == 0): # Line is empty: i.e. blank
            lines[i] = [0] * w
        for j in range(w):
            grid[int(GRID_SIZE/2 - h/2) + i][int(GRID_SIZE/2 - w/2) + j] = lines[i][j]

    return grid

if __name__ == "__main__":
    main()