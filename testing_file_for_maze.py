SCREEN_SIZE = (640, 480)
CELL_SIZE = 32
DEFAULT_CELL = 0b0000000000000000
w_cells = int(SCREEN_SIZE[0] / CELL_SIZE)
h_cells = int(SCREEN_SIZE[1] / CELL_SIZE)

print("Width is {}. Height is {}".format(w_cells,h_cells))


total_cells = w_cells * h_cells

print(total_cells)

maze_array = [DEFAULT_CELL] * total_cells

print(maze_array)

WALL_BITS = 0b0000000000001111
BACKTRACK_BITS = 0b1111000000000000
SOLUTION_BITS = 0b0000111100000000

WALLS = [0b1000, 0b0100, 0b0010, 0b0001]
OPPOSITE_WALLS = [0b0010, 0b0001, 0b1000, 0b0100]
COMPASS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
DIRECTION = ['W', 'S', 'E', 'N']
