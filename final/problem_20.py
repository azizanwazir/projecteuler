############################################################################

# Project Euler Problem 20
# Developer: Azizan Wazir
# Title: Factorial Digit Sum

# Project Euler Website: https://projecteuler.net/problem=20

# Description: Sum of digits in 100!

# Result: Solved
# Time taken to run main function: 0.00 seconds

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
Brute force
'''
def main():
    sum_val = factorial(100)
    sum_str = str(sum_val)
    result = sum([int(x) for x in sum_str])
    log_msg("result", "Sum of digits in 100!: {}".format(result))
    return result
    
                                               
if __name__ == "__main__":
    log_msg("info", "Starting processing of Problem 20")
    start_time = time.time()
    main()
    end_time = time.time() - start_time
    log_msg("info", "Time taken to run main function: {} seconds".format(end_time))
                            