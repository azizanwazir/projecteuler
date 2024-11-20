############################################################################

# Project Euler Problem 17
# Developer: Azizan Wazir
# Title: Number Letter Counts

# Project Euler Website: https://projecteuler.net/problem=17

# Description: How many letters are in all numbers from 1 to 1000 inclusive if written out
#               in words, not counting spaces or hyphens

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

'''
My method
- create a function that converts numbers to written words in accordance with solution definition
    1. Predefine fixed in dictionary: 1 to 19, 20, 30, (n x 10), ... 90, "hundred" suffix, "thousand" suffix
    2. Define text generation as follows:
        a. If number exists in dictionary, return full word

        else
        a. If digit 2 == None or 1: match digit 1 and 2 to dictionary
        b. If digit 2 > 1: match digit 1 to dictionary
                         : match digit 2*10 to dictionary
        c. If digit 3 >= 1: match digit 3 to dictionary, add "hundred" suffix
                          : if digit 1 and 2 != 0, add "and" between digit 3 and 2
        c. if digit 4 == 1: return "one thousand"

- A THOUGHT OCCURED : Instead of returning the word, just return the number of characters in each word

- ... i made a typo on "forty", i made it "fourty" damn it
'''

word_num_dict = {
    '0': 0,       # to add nothing if zero
    '1': 3,       # one 
    '2': 3,       # two
    '3': 5,       # three 
    '4': 4,       # four
    '5': 4,       # five
    '6': 3,       # six
    '7': 5,       # seven
    '8': 5,       # eight
    '9': 4,       # nine
    '10' : 3,     # ten
    '11' : 6,     # eleven
    '12' : 6,     # twelve
    '13' : 8,     # thirteen
    '14' : 8,     # fourteen
    '15' : 7,     # fifteen
    '16' : 7,     # sixteen
    '17' : 9,     # seventeen
    '18' : 8,     # eighteen
    '19' : 8,     # nineteen
    '20' : 6,     # twenty
    '30' : 6,     # thirty
    '40' : 5,     # forty
    '50' : 5,     # fifty
    '60' : 5,     # sixty
    '70' : 7,     # seventy
    '80' : 6,     # eighty
    '90' : 6,     # ninety
    'hundred' : 7,
    'and' : 3,
}

def convert_to_word(i):
    # if in dictionary, return value

    str_i = str(i)
    if word_num_dict.get(str_i):
        return word_num_dict[str_i]

    # start by converting to string and padding with zeros
    digits = str_i.zfill(4)

    digit_1 = digits[3]
    digit_2 = digits[2]
    digit_1_2 = str(int(digits[2] + digits[3])) # remove zeros
    # digit_2 = str(int(digits[2]) * 10)
    digit_3 = digits[1]
    digit_4 = digits[0]

    if digit_4 == '1':
        # must be 1000
        return 3 + 8 # one thousand

    if digit_3 != '0':
        if digit_1 == '0' and digit_2 == '0':
            # x-hundred
            return word_num_dict[digit_3] + word_num_dict['hundred']
        else:
            # check two digit in dictionary first
            last_two_sum = 0
            if word_num_dict.get(digit_1_2):
                last_two_sum = word_num_dict.get(digit_1_2)
            else:
                last_two_sum = word_num_dict[digit_1] + word_num_dict[digit_2 + "0"]

            return word_num_dict[digit_3] + word_num_dict['hundred'] + word_num_dict['and'] + last_two_sum
    
    if digit_2 != '0':
        last_two_sum = 0
        # print(digit_1, digit_2, digit_1_2)
        if word_num_dict.get(digit_1_2):
            last_two_sum = word_num_dict.get(digit_1_2)
            return last_two_sum
        else:
            last_two_sum = word_num_dict[digit_1] + word_num_dict[digit_2 + "0"]
            return last_two_sum
    
    # should not reach this point
    if digit_2 == '0':
        return word_num_dict[digit_1]


def main():
    letter_sum = 0

    for i in range(1,1001):
        letter_sum += convert_to_word(i)
    
    log_msg("result", "Number of letters used: {}".format(letter_sum))
    return letter_sum

                                               
if __name__ == "__main__":
    log_msg("info", "Starting processing of Problem 17")
    start_time = time.time()
    main()
    end_time = time.time() - start_time
    log_msg("info", "Time taken to run main function: {} seconds".format(end_time))
                            