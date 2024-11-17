############################################################################

# Project Euler Problem 4
# Developer: Azizan Wazir
# Title: Largest Palindrome Product

# Project Euler Website: https://projecteuler.net/problem=4

# Description: Find largest palindrome made from the product of two 3-digit numbers (e.g. 9009 = 91 x 99)

# Result: Solved
# Time taken to run main function: 0.002000570297241211 seconds

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
1. Get value of 999 x 999 (= 998001)
2. Get next lowest palindrome by reducing 3rd digit of the number, e.g. 998001 --> 997 799
    2a. If third digit == 0, set 3rd digit to 9, reduce second digit by 1
    2b. If second digit == 0, set 2nd and 3rd digit to 9, reduce first digit by 1
    2c. If first digit == 0, ignore as lowest possible value for 3-digit x 3-digit = 10,000

3. Check if next lowest palindrome (NLP) is divisible by next highest 3-digit number (NHN) (starting with NHN = 999).
4. If divisible, m = NHN and n = NLP / NHN is the answer
5. If not divisible, check if NLP / NHN > 999.
6. If yes, repeat from step 2.
7. If no, set NHN = NHN - 1 and repeat from step 3.

'''

def main():
    start_value = 999 * 999
    first_three_digits = [int(x) for x in list(str(start_value)[:3])]

    # repeat until found
    while(True):
        if first_three_digits[2] == 0:
            if first_three_digits[1] == 0:
                if first_three_digits[0] != 0:
                    first_three_digits[0] -= 1
                    first_three_digits[1] = 9
                    first_three_digits[2] = 9
                else:
                    log_msg("error", "Reached 4 digit numbers. Something went wrong.")
                    return -1
            else:
                first_three_digits[1] -= 1
                first_three_digits[2] = 9
        else:
            first_three_digits[2] = first_three_digits[2] - 1

        next_lowest_palindrome = [str(x) for x in first_three_digits] + [str(x) for x in first_three_digits[::-1]]
        next_lowest_palindrome = "".join(next_lowest_palindrome)
        next_lowest_palindrome = int(next_lowest_palindrome)

        for i in range(999, 1, -1):
            remainder = next_lowest_palindrome % i 
            if remainder == 0:
                divisor = next_lowest_palindrome // i
                if divisor > 1000:
                    # log_msg("debug", "Current palindrome: {}. Factors: {}, {}".format(str(next_lowest_palindrome), str(i), str(divisor)))
                    break
                else:
                    log_msg("result", "Largest palindrome: {}. Factors: {}, {}".format(str(next_lowest_palindrome), str(i), str(divisor)))
                    return 0
                                               
if __name__ == "__main__":
    log_msg("info", "Starting processing of Problem 4")
    start_time = time.time()
    main()
    end_time = time.time() - start_time
    log_msg("info", "Time taken to run main function: {} seconds".format(end_time))
                            