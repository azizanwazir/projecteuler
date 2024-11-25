############################################################################

# Project Euler Problem 21
# Developer: Azizan Wazir
# Title: Amicable Numbers

# Project Euler Website: https://projecteuler.net/problem=21

# Description: Sum of all amicable numbers under 10,000

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
d(n) = sum of proper divisors of n
if d(a) = b and d(b) = a where a != b, (a,b) are an amicable pair
a and b are called amicable numbers

My method:
1. 
'''
def main():
    pass
                                               
if __name__ == "__main__":
    log_msg("info", "Starting processing of Problem 21")
    start_time = time.time()
    main()
    end_time = time.time() - start_time
    log_msg("info", "Time taken to run main function: {} seconds".format(end_time))
                            