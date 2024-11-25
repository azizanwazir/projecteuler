############################################################################

# Project Euler Problem 18
# Developer: Azizan Wazir
# Title: Maximum Path Sum I

# Project Euler Website: https://projecteuler.net/problem=18

# Description: Find the max total of vertical path in a triangle of numbers

# Result: 
# Time taken to run main function: 

############################################################################

import time
from datetime import datetime 
from math import factorial

# for custom command line logging                            
def log_msg(status, msg):
    date_str = datetime.strftime(datetime.now(), "%d %b %Y %H:%M:%S")
    status = status.upper().ljust(8)
    print("{} :: {} - {}".format(date_str, status, msg))

'''
My method
Initial thoughts
    - First thought is just go down the rows and add the highest of the two possible numbers
    - issue is that highest of two choices may not reach the highest options in the next row
    - 
'''

# brute force method to return best path
def brute_force(triangle):
    n_rows = len(triangle)
    n_permutations = factorial(n_rows - 1)
    paths = [[triangle[0][0]] for i in range(n_permutations)] # pre-initialise with first value
    
    # iterate over rows
    for i in range(1, n_rows):
        current_perm = 0
        row = triangle[i]
        # iterate over max columns
        for j in range(0, len(row)):
            paths[i]



def main():
    pass
                                               
if __name__ == "__main__":
    log_msg("info", "Starting processing of Problem 18")
    start_time = time.time()
    main() 
    end_time = time.time() - start_time
    log_msg("info", "Time taken to run main function: {} seconds".format(end_time))
                            