############################################################################

# Project Euler Problem 2
# Developer: Azizan Wazir
# Title: Even Fibonacci Numbers

# Project Euler Website: https://projecteuler.net/problem=2

# Description: Find sum of even-valued Fibonacci numbers under 4,000,000

# Result: Solved
# Time taken to run main function: 0.00099945068359375 seconds

############################################################################

import time
from datetime import datetime

# for custom command line logging                            
def log_msg(status, msg):
    date_str = datetime.strftime(datetime.now(), "%d %b %Y %H:%M:%S")
    status = status.upper().ljust(8)
    print("{} :: {} - {}".format(date_str, status, msg))
                            
def main():
    # F(n) = f_n = Fibonacci number N
    # Problem skips Fibonacci number 0, which is 1 
    f_n = 1 # F(N)
    f_n1  = 2 # F(N+1)
    f_n2 = f_n + f_n1

    final_sum = 2 # initialise with F(2)

    while f_n2 < 4000000:
        
        if f_n2 % 2 == 0:
            final_sum += f_n2

        f_n = f_n1
        f_n1 = f_n2
        f_n2 = f_n + f_n1

    log_msg("result", "Final answer: {}".format(str(final_sum)))
                                               
if __name__ == "__main__":
    log_msg("info", "Starting processing of Problem 2")
    start_time = time.time()
    main()
    end_time = time.time() - start_time
    log_msg("info", "Time taken to run main function: {} seconds".format(end_time))
                            