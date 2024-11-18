############################################################################

# Project Euler Problem 7
# Developer: Azizan Wazir
# Title: 10001st Prime

# Project Euler Website: https://projecteuler.net/problem=7

# Description: What is the 10,001st prime number (where 2 is the first prime number)

# Result: Solved
# Time taken to run main function: 1.3405983448028564 seconds

############################################################################

import time
from datetime import datetime

# for custom command line logging                            
def log_msg(status, msg):
    date_str = datetime.strftime(datetime.now(), "%d %b %Y %H:%M:%S")
    status = status.upper().ljust(8)
    print("{} :: {} - {}".format(date_str, status, msg))

# reusing some code from Problem 5
'''
My method:
1. Create a list of prime numbers and pre-fill with value 2, P(1) = 2
2. For odd number n , Odd(n), starting with Odd(1) = 3
    2a. If Odd(n) is divisible by P(1), skip to step 4
    2b. Else, repeat step 2a until end of list of primes.
    2c. If reached end of list of primes, go to step 3
3. Add Odd(n) to list of primes
4. Increment n by 2, then repeat step 2 until length of list of primes == 10,001
5. Return P(10,001)
'''

def main():
    target_no = 10001
    prime_list = [2]
    # prime_len = 1 decided not to use this because len(list) has time complexity O(1)

    is_prime = True

    i = 3
    while len(prime_list) != target_no: # go until target prime is found
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
    
    log_msg("result", "10,001th Prime Number: {}".format(prime_list[-1]))
    return prime_list[-1]
                                               
if __name__ == "__main__":
    log_msg("info", "Starting processing of Problem 7")
    start_time = time.time()
    main()
    end_time = time.time() - start_time
    log_msg("info", "Time taken to run main function: {} seconds".format(end_time))
                            