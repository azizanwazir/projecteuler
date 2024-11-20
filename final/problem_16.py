############################################################################

# Project Euler Problem 16
# Developer: Azizan Wazir
# Title: Power Digit Sum

# Project Euler Website: https://projecteuler.net/problem=16

# Description: What is the sum of the digits of the number 2^1000

# Result: Solved
# Time taken to run main function: 0.0014028549194335938 seconds

############################################################################

import time
from datetime import datetime

# for custom command line logging                            
def log_msg(status, msg):
    date_str = datetime.strftime(datetime.now(), "%d %b %Y %H:%M:%S")
    status = status.upper().ljust(8)
    print("{} :: {} - {}".format(date_str, status, msg))

# lets try brute force
# Result: brute force works
def main():
    result_value = 2**1000
    result_str = str(result_value)
    result_list = [int(x) for x in result_str]
    result = sum(result_list)

    log_msg("result", "Sum of digits: {}".format(result))
    return result
                                               
if __name__ == "__main__":
    log_msg("info", "Starting processing of Problem 16")
    start_time = time.time()
    main()
    end_time = time.time() - start_time
    log_msg("info", "Time taken to run main function: {} seconds".format(end_time))
                            