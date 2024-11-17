############################################################################

# Project Euler Problem 162
# Developer: Azizan Wazir
# Title: Hexadecimal Numbers

# Project Euler Website: https://projecteuler.net/problem=162

# Description: 

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

def main():
    pass
                                               
if __name__ == "__main__":
    log_msg("info", "Starting processing of Problem 162")
    start_time = time.time()
    main()
    end_time = time.time() - start_time
    log_msg("info", "Time taken to run main function: {} seconds".format(end_time))
                            