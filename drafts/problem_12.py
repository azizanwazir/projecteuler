############################################################################

# Project Euler Problem 12
# Developer: Azizan Wazir
# Title: Highly Divisible Triangular Number

# Project Euler Website: https://projecteuler.net/problem=12

# Description: Find value of first triangle number with over 500 divisors
# Triangle number T(n) = sum(natural numbers from 1 to n)

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
Initial thoughts:
    - Try brute force first. After previous solution, maybe this is just algorithmic thinking practice
    - Set base number as double of the target number of divisors as the number needs to be at least the number of divisors
        but if it is not prime, number of factors will be reduced by at least half 

First iteration:
    - Tried brute force but not feasible.
    - If number can be expressed as N = x^a + y^b + z^c + ..., then
        number of factors = (a + 1) * (b + 1) * (c + 1) *...
    
    Therefore, we need to find a number where (a + 1) * (b + 1) ... >= 500
        sample cases:
        try (a+1) == (b+1) == c --> c^2 >= 500
                                    c   >= 22.36

    Triangular number formula:
    T(1) = 1                             = 1 
    T(2) = 1 + 2                         = 3 
    T(3) = 1 + 2 + 3                     = 6 
    T(4) = 1 + 2 + 3 + 4                 = 10
    T(5) = 1 + 2 + 3 + 4 + 5             = 15
    T(6) = 1 + 2 + 3 + 4 + 5 + 6         = 21
    T(7) = 1 + 2 + 3 + 4 + 5 + 6 + 7     = 28
    T(8) = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 = 36
    T(n) = n(n+1)/2 # HAD TO SEARCH IT UP crap

'''
    
def main():
    tn = 1 # initialise triangular number
    n = 1

    while(tn < 10000):
        n += 1
        tn += n

    log_msg("debug", "Using T({}) = {}".format(n, tn))
    factors = []

    while(True):
        log_msg("debug", "Trying T({}) = {}".format(n, tn))
        for i in range(1, tn//2):
            if tn % i == 0:
                factors.append(i)
        
        log_msg("debug", "Number of factors = {}".format(len(factors)))
        if len(factors) > 200:
            break

        # if reaches this point, increment to next tn and reset factors
        n += 1
        tn += n
        factors = []
    
    log_msg("result", "Smallest triangular number with over 500 factors: {}".format(tn))


if __name__ == "__main__":
    log_msg("info", "Starting processing of Problem 12")
    start_time = time.time()
    main()
    end_time = time.time() - start_time
    log_msg("info", "Time taken to run main function: {} seconds".format(end_time))
                            