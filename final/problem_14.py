############################################################################

# Project Euler Problem 14
# Developer: Azizan Wazir
# Title: Longest Collatz Sequence

# Project Euler Website: https://projecteuler.net/problem=14

# Description: Which starting number under 1 mil produces the longest chain with the following iterative sequence
#   n --> n /2      (n is even)
#   n --> 3n + 1    (n is odd)

# Result: Solved
# Time taken to run main function: 2.14s

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
1. Create a dictionary of Collatz numbers (Cd) with keys 1 to 999,999, value 0. set Cd[1] = 1
2. Set max chain length and max chain length original number (n) to 0
3. For n, set chain length = 0
    3a. if Cd[n] == 0 (not yet computed), 
        a. If even, set n = n/2, increment chain length by 1
        b. If odd, set n = 3n - 1, increment chain length by 1
        c. Repeat step 2 with new n until n == 1, then set Cd[original n] = chain length
    3b. if Cd[n] != 0 (already computed),
        a. add Cd[n] to chain length and set Cd[original n] = chain length
4. If chain length > max chain length, replace max chain length and max chain length original number
5. Repeat step 2 to 4 until all values in dictionary populated
6. Return max chain length original number
'''

def main():
    collatz_dict = {x:0 for x in range(1, 1000000)}
    collatz_dict[1] = 1
    # add values for powers of 2
    # 2**0 == 1
    # 2**1 == 2
    # 2**m == m + 1
    n = 2
    m = 0
    max_chain = 0
    max_chain_number = 0
    # while(n < 1000000):
    #     n = 2**m
    #     collatz_dict[n] = m + 1
    #     if m + 1 > max_chain:
    #         max_chain = m + 1
    #     # log_msg("debug", "Collatz[{}] = {}".format(n, m + 1))
        
    #     odd_n = (n - 1)/3
    #     if odd_n == 0:
    #         continue

    #     if odd_n == int(odd_n):
    #         if collatz_dict[int(odd_n)] == 0:
    #             collatz_dict[int(odd_n)] = m + 2
    #             # log_msg("debug", "Collatz[{}] = {}".format(int(odd_n), m + 2))
    #             if m + 2 > max_chain:
    #                 max_chain = m + 2
        
        
    #     n += 1
    #     m += 1
    
    all_keys = list(collatz_dict.keys())#[:100]
    # all_keys.reverse()

    for collatz_n in all_keys:
        chain_length = collatz_dict[collatz_n]
        n = collatz_n
        if chain_length == 0: # not yet initialised
            while(n != 1):
                if collatz_dict.get(n) != 0 and collatz_dict.get(n) != None:
                    # print("Collatz length ({}): {} + ({}){} = {}".format(collatz_n, chain_length, n, collatz_dict[n], chain_length + collatz_dict[n]))
                    chain_length += collatz_dict[n] - 1 # adjustment already accounted for
                    break

                if n % 2 == 0:
                    n = n / 2
                    chain_length += 1
                else:
                    n = 3*n + 1
                    chain_length += 1

            collatz_dict[collatz_n] = chain_length + 1
            if max_chain < collatz_dict[collatz_n]:
                max_chain = collatz_dict[collatz_n]
                max_chain_number = collatz_n
    
    log_msg("result", "Max chain: {}, Max chain number: {}".format(max_chain, max_chain_number))
    return max_chain
    
                


        


    
    

        

                                               
if __name__ == "__main__":
    log_msg("info", "Starting processing of Problem 14")
    start_time = time.time()
    main()
    end_time = time.time() - start_time
    log_msg("info", "Time taken to run main function: {} seconds".format(end_time))
                            