import maze
import generate_maze
import sys
import random


# Solve maze using Pre-Order DFS algorithm, terminate with solution
# also will try to do this recursively
def solve_dfs(m):
    """mostly have to make use of refractoring the code in """
    # TODO: Implement solve_dfs
    # not in bit form just yet but this wil make it easier
    current = 0
    visited = 0
    # stack as a list  for keeping strack of the visited cells
    visited_stack= list()

    # while the currrect cell in the loop hast gotten to be the value of the solution bit( the solutuon square in the matrix)
    # low key should make this into a helper of some sort since its being called more than once and could make my code more modular
    while current is not SOLUTION_BITS:
        # make a list of the yet to be visited cells by calling the cell_neighbors method to set the current cells neighbors
        unvisited_cells = m.cell_neighbors(current)
        # while there are still unvisited neigbors in the list of neigbors
        if len(unvisited_neighbors) >= 1:
            # choose random neighbor to be new cell
    		new_cell_index = random.randint(0, len(unvisited_neighbors) - 1)
            new_cell, compass_index = unvisited_neighbors[new_cell_index]

    pass
# Solve maze using BFS algorithm, terminate with solution
def solve_bfs(m):
    # TODO: Implement solve_bfs
    pass


def print_solution_array(m):
    solution = m.solution_array()
    print('Solution ({} steps): {}'.format(len(solution), solution))


def main(solver='dfs'):
    current_maze = maze.Maze('create')
    generate_maze.create_dfs(current_maze)
    if solver == 'dfs':
        solve_dfs(current_maze)
    elif solver == 'bfs':
        solve_bfs(current_maze)
    while 1:
        maze.check_for_exit()
    return

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main()
