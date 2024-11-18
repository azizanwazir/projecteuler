############################################################################

# Project Euler Problem 8
# Developer: Azizan Wazir
# Title: Largest Product in a Series

# Project Euler Website: https://projecteuler.net/problem=8

# Description: Find the thirteen adjacent digits in the 1000 digit number
#               that have the greatest product and return the product

# Result: Solved
# Time taken to run main function: 0.0010001659393310547 seconds

############################################################################

import time
from datetime import datetime
# imports for multiplying objects in list
from functools import reduce
from operator import mul

# for custom command line logging                            
def log_msg(status, msg):
    date_str = datetime.strftime(datetime.now(), "%d %b %Y %H:%M:%S")
    status = status.upper().ljust(8)
    print("{} :: {} - {}".format(date_str, status, msg))


'''
My Method:
1. Divide the number into sections using 0 as the delimiter
2. Remove any sections that have less than 13 digits
3. Set highest product to 0
4. For section n, S(n), get product of first set of 13 digits.
5. If product > highest product, replace highest product.
6. Repeat step 4 and 5 for each set of 13 digits until end of section.
7. Repeat steps 4 to 6 for each section
8. Return highest product
    
'''

def main():
    target_no = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"
    target_sections = target_no.split("0")
    target_sections = [x for x in target_sections if len(x) > 13]

    highest_product = 0
    for section in target_sections:
        for i in range(0, len(section) - 12):
            subsection = [int(x) for x in section[i:i+13]]
            product = reduce(mul, subsection)
            if product > highest_product:
                highest_product = product

    log_msg("result", "Highest product: {}".format(highest_product))
    return highest_product



                                               
if __name__ == "__main__":
    log_msg("info", "Starting processing of Problem 8")
    start_time = time.time()
    main()
    end_time = time.time() - start_time
    log_msg("info", "Time taken to run main function: {} seconds".format(end_time))
                            