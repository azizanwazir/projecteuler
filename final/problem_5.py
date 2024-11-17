############################################################################

# Project Euler Problem 5
# Developer: Azizan Wazir
# Title: Smallest Multiple

# Project Euler Website: https://projecteuler.net/problem=5

# Description: Find smallest positive number that is evenly divisible by all numbers from 1 to 20

# Result: Solved
# Time taken to run main function: 0.001005411148071289 seconds

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
1. Get all prime factors for first number (n = 1)
2. If prime factor is not key in prime factor dictionary:
    2a. Add prime factors as key to prime factor dictionary and 1 as the value
    2b. If n / prime factor is not in prime factor dictionary:
        2bi. If n / prime factor 
3. If prime factor is key in prime factor dictionary:
    3a. If count of prime factor > value in dictionary, replace value with count of prime factor
4. Repeat steps 1 to 3 until x (in this case, 20)
5. Multiply dictionary key and value and sum all together for final result

'''



def main():
    prime_dict = {2:1}
    final_sum = 1
    is_prime = True

    n = 20

    for i in range(3, n):
        is_prime = True

        for prime in prime_dict.keys():
            if i % prime == 0:
                is_prime = False
                # if number is not a prime
                check_i = i
                count = 0

                while(check_i % prime == 0 & check_i != prime):
                    check_i = check_i // prime
                    count += 1

                if prime_dict[prime] < count:
                    prime_dict[prime] = count
                # print(i, prime_dict)
                continue
        if is_prime:
            prime_dict[i] = 1
            
    for prime in prime_dict.keys():
        final_sum = final_sum * (prime ** prime_dict[prime])
    
    log_msg("debug", "Prime dictionary: {}".format(prime_dict))
    log_msg("result", "Smallest positive number evenly divisible by all number from 1 to {}: {}".format(n, final_sum))


                                               
if __name__ == "__main__":
    log_msg("info", "Starting processing of Problem 5")
    start_time = time.time()
    main()
    end_time = time.time() - start_time
    log_msg("info", "Time taken to run main function: {} seconds".format(end_time))
                            