############################################################################

# Project Euler Problem 10
# Developer: Azizan Wazir
# Title: Summation of Primes

# Project Euler Website: https://projecteuler.net/problem=10

# Description: Find sum of all primes below 2 million

# Result: Solved
# Time taken to run main function: 299.60577750205994 seconds

# Comments: BRUTE FORCE. Not sure if there was a better way to do this.

############################################################################

import time
from datetime import datetime

# for custom command line logging                            
def log_msg(status, msg):
    date_str = datetime.strftime(datetime.now(), "%d %b %Y %H:%M:%S")
    status = status.upper().ljust(8)
    print("{} :: {} - {}".format(date_str, status, msg))

# reusing some code from Problem 7
def main():
    target_no = 2000000
    prime_list = [2]
    # prime_len = 1 decided not to use this because len(list) has time complexity O(1)

    is_prime = True

    i = 3
    while i < target_no: # go until target prime is found
        # bool to indicate if add to dictionary or not
        is_prime = True

        # iterate through all non-null values in prime dictionary
        for prime in prime_list:
            if i % prime == 0:
                is_prime = False
                break

        if is_prime:
            prime_list.append(i)
        
        # increase by 2 to get to next odd number
        i += 2
    
    sum_primes = sum(prime_list)
    log_msg("result", "Sum of primes below 2,000,000: {}".format(sum_primes))
    return sum_primes
                                               
if __name__ == "__main__":
    log_msg("info", "Starting processing of Problem 10")
    start_time = time.time()
    main()
    end_time = time.time() - start_time
    log_msg("info", "Time taken to run main function: {} seconds".format(end_time))
                            