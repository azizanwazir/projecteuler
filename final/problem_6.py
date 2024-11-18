############################################################################

# Project Euler Problem 6
# Developer: Azizan Wazir
# Title: Sum Square Difference

# Project Euler Website: https://projecteuler.net/problem=6

# Description: Difference between the sum of squares of first 100 natural numbers 
#               and the square of the sum

# Result: Solved
# Time taken to run main function: 0.0010001659393310547 seconds

############################################################################

import time
from datetime import datetime

# for custom command line logging                            
def log_msg(status, msg):
    date_str = datetime.strftime(datetime.now(), "%d %b %Y %H:%M:%S")
    status = status.upper().ljust(8)
    print("{} :: {} - {}".format(date_str, status, msg))

def main():
    limit = 100 
    list_of_numbers = range(1, limit + 1) # python Range(m, n) goes from m to n-1

    sum_squares = sum([x**2 for x in list_of_numbers])
    square_sums = sum(list_of_numbers)**2

    difference = abs(sum_squares - square_sums)
    log_msg("result", "Difference of Sum of Squares - Square of Sums: {}".format(difference))
    return difference

                                               
if __name__ == "__main__":
    log_msg("info", "Starting processing of Problem 6")
    start_time = time.time()
    main()
    end_time = time.time() - start_time
    log_msg("info", "Time taken to run main function: {} seconds".format(end_time))
                            