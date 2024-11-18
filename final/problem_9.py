############################################################################

# Project Euler Problem 9
# Developer: Azizan Wazir
# Title: Special Pythagorean Triplet

# Project Euler Website: https://projecteuler.net/problem=9

# Description: Find product of Pythagorean triplet (a, b, c where a^2 + b^2 = c^2) 
#               where a+b+c = 1000

# Result: Solved
# Time taken to run main function: 0.10970950126647949 seconds

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
-- Background
    a < b < c
    a^2 + b^2 = c^2, therefore sqrt(a^2 + b^2) = c, where c is a natural number
    c = 1000 - a - b, therefore c < 1000
    sqrt(a^2 + b^2) < 1000
    a^2 + b^2 < 1,000,000
    since a < b, a, b < sqrt(1,000,000 / 2)
    a, b < 707.1067
    a, b < 707 


1. For a, b (starting with min_start = 707 --> a = min_start - 1, b = min_start)
2. If sqrt(a^2 + b^2) == int(sqrt(a^2 + b^2))
    2a. set c = sqrt(a^2 + b^2)
    2b. if a + b + c = 1000, return a*b*c
    2c. If a + b + c < 1000, go to step 4, otherwise go to step 3
3. Decrement a by 1, repeat step 2
4. Set a = min_start - 2, b = min_start - 1
5. Repeat step 2
'''

def main():
    target_number = 1000
    min_start = 1000**2 # c^2 < 1,000,000 because c = 1000 - a - b, where a,b < 0
    min_start = (min_start/2)**0.5 # because c < sqrt(2a^2), because a < b      
    min_start = int(min_start) # round down to nearest integer

    i = 0 # base decrement
    j = 1 # walking increment to continuously reduce a

    a = min_start - i - j
    b = min_start - i
    c = target_number

    while(True):
        c = (a**2 + b**2)**0.5

        if a + b + c < target_number or (a == 0) or (b == 0):
            i += 1
            j = 1
            a = min_start - i - j
            b = min_start - i

        if j == 1 and a + b + c < target_number:
            log_msg("error", "Could not find target number. Last test: a={}, b={}".format(a,b))
            return -1

        if int(c) == c:
            if a + b + c == target_number:
                break
            else:
                j += 1
                a = min_start - i - j
        else:
            j += 1
            a = min_start - i - j

    final_product = int(a*b*c)
    log_msg("result", "Highest product: {}. Factors: {}, {}, {}". format((final_product), a, b, c))
    return final_product

if __name__ == "__main__":
    log_msg("info", "Starting processing of Problem 9")
    start_time = time.time()
    main()
    end_time = time.time() - start_time
    log_msg("info", "Time taken to run main function: {} seconds".format(end_time))
