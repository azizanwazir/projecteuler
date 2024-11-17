############################################################################

# Project Euler Problem 3
# Developer: Azizan Wazir
# Title: Largest Prime Factor

# Project Euler Website: https://projecteuler.net/problem=3

# Description: Largest prime factor of 600851475143

# Result: Solved
# Time taken to run main function: 0.15014362335205078 seconds

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
0. Initialise list of prime numbers with [2, 3] and latest_prime = 3
1. Divide target_no by first prime number, P(n).
2. If evenly divisible, set target_no = target_no / P(n) and repeat from step 1.
3. If not evenly divisible, get next odd number and check if divisible by any number in list of prime numbers.
4. If next odd number is equal to target_no, largest prime number is next odd number.
5. If next odd number is not equal to target_no and not evenly divisible by any number in list of prime numbers, 
    add it to the list of prime numbers, 
    set it as latest pirime, 
    then repeat from step 1.

'''

def main():
    target_no = 600851475143
    list_of_primes = [2, 3]
    latest_prime = 3
    next_odd = latest_prime + 2

    # repeat until target_no is 1
    while(target_no != 1):

        if target_no % latest_prime != 0:
            
            # check if next odd is prime
            next_odd = latest_prime + 2
            
            # repeat until next prime is found
            for prime in list_of_primes:
                if next_odd % prime != 0:
                    continue
            
            list_of_primes.append(next_odd)
            latest_prime = next_odd

        else:
            if latest_prime == target_no:
                log_msg("result", "Largest prime: {}".format(str(latest_prime)))
                # log_msg("info", "List of primes: {}".format(", ".join([str(x) for x in list_of_primes])))
                return latest_prime
            
            target_no = target_no / latest_prime
                            
                                               
if __name__ == "__main__":
    log_msg("info", "Starting processing of Problem 3")
    start_time = time.time()
    main()
    end_time = time.time() - start_time
    log_msg("info", "Time taken to run main function: {} seconds".format(end_time))
                            