############################################################################

# Project Euler Problem 1
# Developer: Azizan Wazir
# Title: Multiples of 3 or 5

# Project Euler Website: https://projecteuler.net/archives

# Description: Find the sum of all the multiples of 3 or 5 below 1000

# Result: Solved
# Time taken to run main function: 0.0010013580322265625 seconds

############################################################################

import time
from datetime import datetime

# for custom command line logging                            
def log_msg(status, msg):
    date_str = datetime.strftime(datetime.now(), "%d %b %Y %H:%M:%S")
    status = status.upper().ljust(8)
    print("{} :: {} - {}".format(date_str, status, msg))
                            
def main():
    final_sum = 0

    # skip 0 and stop BEFORE 1000
    for i in range(1, 1000):
        if i % 3 == 0 or i % 5 == 0:
            final_sum +=  i
    
    log_msg("result", "Final answer: {}".format(str(final_sum)))

                                               
if __name__ == "__main__":
    log_msg("info", "Starting processing of Problem 1")
    start_time = time.time()
    main()
    end_time = time.time() - start_time
    log_msg("info", "Time taken to run main function: {} seconds".format(end_time))
                            