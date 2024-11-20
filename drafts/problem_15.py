############################################################################

# Project Euler Problem 15
# Developer: Azizan Wazir
# Title: Lattice Paths

# Project Euler Website: https://projecteuler.net/problem=15

# Description: Only moving right and down, how many routes are there from the top left
#               to bottom right corner of a 20 x 20 grid

# Result: 
# Time taken to run main function: 

############################################################################

import time
from datetime import datetime

# for custom command line logging                            
def log_msg(status, msg):
    date_str = datetime.strftime(datetime.now(), "%d %b %Y %H:%M:%S")
    status = status.upper().ljust(8)
    print("{} :: {} - {}".format(date_str, status, msg))

'''
My method:
Solved on paper.
    - Given that only right and down are allowed, once the arrow reaches the right
        or bottom border, there is only 1 path left
    - At the top left, there will be 2 possible paths (routes = 2)
    - From the two paths, if not yet at the borders, there are 2 more paths each
        routes = 2 + 2 + 2
    - From the resulting paths, any paths not at the borders will have 2 more paths
        routes = 2 + 2(number of nodes NOT at border)
    - number of nodes that are not at the bottom row or right row =
        all in lattice except nodes on bottom row or right row (duh)
    - i.e., number of nodes NOT at border = (grid length) x (grid length)
            because number of nodes = grid length + 1

'''

def main():
    grid_size = 4
    routes = 2*(grid_size)**2 - 2
    log_msg("result", "Number of paths in a {}x{} grid: {}".format(grid_size, grid_size, routes))
    return routes

                                               
if __name__ == "__main__":
    log_msg("info", "Starting processing of Problem 15")
    start_time = time.time()
    main()
    end_time = time.time() - start_time
    log_msg("info", "Time taken to run main function: {} seconds".format(end_time))
                            