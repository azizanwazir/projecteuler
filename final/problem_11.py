############################################################################

# Project Euler Problem 11
# Developer: Azizan Wazir
# Title: Largest Product in a Grid

# Project Euler Website: https://projecteuler.net/problem=11

# Description: Greatest product of four adjacent numbers in same direction (up, down, left, right, diagonal)

# Result: Solved
# Time taken to run main function: 0.0010008811950683594 seconds

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
** Initial thoughts
    - Brute forcing the whole grid will definitely work, but the time complexity would be around O(n^4) as most items would be checked in at least 3 directions (down, right, diagonal down, diagonal up)
    - Removing combinations that have "00" would reduce the number of permutations
    - Removing combinations that have low digits, e.g. "01" may work as it would reduce the number less likely permutations, however something like 99 x 99 x 99 x 1 would still be higher than 31 x 31 x 31 x 31
    - Potentially we could start by looking for the largest numbers, i.e. start from 99, search for nearby combinations, then 98, etc. but how would we know where to stop?
    - Possibly subtracting all values by the average and searching for values that are above 0 could work.

My method:
1. Find average of entire grid
2. Subtract average from entire grid, if less than 0 set to 0
3. Repeat steps 1 and 2 two more times
4. Set max product = 0
5. If cell != 0, check cell product down, right, diagonally right and diagonally left
6. If product > latest max product, update max product
7. Repeat for all cells

Observations:
- Using the average reduction method, I got a near instant correct result.
- HOWEVER, removing all the reductions, I still got a 0.0010235309600830078 seconds result.
- Sometimes brute force is good enough lmao

'''

def main():
    grid = [["08", "02", "22", "97", "38", "15", "00", "40", "00", "75", "04", "05", "07", "78", "52", "12", "50", "77", "91", "08"],
            ["49", "49", "99", "40", "17", "81", "18", "57", "60", "87", "17", "40", "98", "43", "69", "48", "04", "56", "62", "00"],
            ["81", "49", "31", "73", "55", "79", "14", "29", "93", "71", "40", "67", "53", "88", "30", "03", "49", "13", "36", "65"],
            ["52", "70", "95", "23", "04", "60", "11", "42", "69", "24", "68", "56", "01", "32", "56", "71", "37", "02", "36", "91"],
            ["22", "31", "16", "71", "51", "67", "63", "89", "41", "92", "36", "54", "22", "40", "40", "28", "66", "33", "13", "80"],
            ["24", "47", "32", "60", "99", "03", "45", "02", "44", "75", "33", "53", "78", "36", "84", "20", "35", "17", "12", "50"],
            ["32", "98", "81", "28", "64", "23", "67", "10", "26", "38", "40", "67", "59", "54", "70", "66", "18", "38", "64", "70"],
            ["67", "26", "20", "68", "02", "62", "12", "20", "95", "63", "94", "39", "63", "08", "40", "91", "66", "49", "94", "21"],
            ["24", "55", "58", "05", "66", "73", "99", "26", "97", "17", "78", "78", "96", "83", "14", "88", "34", "89", "63", "72"],
            ["21", "36", "23", "09", "75", "00", "76", "44", "20", "45", "35", "14", "00", "61", "33", "97", "34", "31", "33", "95"],
            ["78", "17", "53", "28", "22", "75", "31", "67", "15", "94", "03", "80", "04", "62", "16", "14", "09", "53", "56", "92"],
            ["16", "39", "05", "42", "96", "35", "31", "47", "55", "58", "88", "24", "00", "17", "54", "24", "36", "29", "85", "57"],
            ["86", "56", "00", "48", "35", "71", "89", "07", "05", "44", "44", "37", "44", "60", "21", "58", "51", "54", "17", "58"],
            ["19", "80", "81", "68", "05", "94", "47", "69", "28", "73", "92", "13", "86", "52", "17", "77", "04", "89", "55", "40"],
            ["04", "52", "08", "83", "97", "35", "99", "16", "07", "97", "57", "32", "16", "26", "26", "79", "33", "27", "98", "66"],
            ["88", "36", "68", "87", "57", "62", "20", "72", "03", "46", "33", "67", "46", "55", "12", "32", "63", "93", "53", "69"],
            ["04", "42", "16", "73", "38", "25", "39", "11", "24", "94", "72", "18", "08", "46", "29", "32", "40", "62", "76", "36"],
            ["20", "69", "36", "41", "72", "30", "23", "88", "34", "62", "99", "69", "82", "67", "59", "85", "74", "04", "36", "16"],
            ["20", "73", "35", "29", "78", "31", "90", "01", "74", "31", "49", "71", "48", "86", "81", "16", "23", "57", "05", "54"],
            ["01", "70", "54", "71", "83", "51", "54", "69", "16", "92", "33", "48", "61", "43", "52", "01", "89", "19", "67", "48"]]
    
    # convert to integers
    grid_int = [[int(x) for x in grid_line] for grid_line in grid]
    grid_average = sum([sum(grid_line) for grid_line in grid_int]) / (len(grid)*len(grid[0]))

    # reduce by average 3 times total
    grid_int_reduced = [[x - grid_average if x - grid_average > 0 else 0 for x in grid_line] for grid_line in grid_int]

    non_zero_count = [[1 for x in grid_line if x > 0] for grid_line in grid_int_reduced]
    non_zero_count = sum([sum(grid_line) for grid_line in non_zero_count])
    grid_average = sum([sum(grid_line) for grid_line in grid_int_reduced]) / non_zero_count
    grid_int_reduced = [[x - grid_average if x - grid_average > 0 else 0 for x in grid_line] for grid_line in grid_int_reduced] 
    
    non_zero_count = [[1 for x in grid_line if x > 0] for grid_line in grid_int_reduced]
    non_zero_count = sum([sum(grid_line) for grid_line in non_zero_count])
    grid_average = sum([sum(grid_line) for grid_line in grid_int_reduced]) / non_zero_count
    grid_int_reduced = [[x - grid_average if x - grid_average > 0 else 0 for x in grid_line] for grid_line in grid_int_reduced] 

    max_product = 0
    # iterate over reduced grid, then match to main grid if found
    for i in range(0, 20):
        for j in range(0, 20):
            if grid_int_reduced[i][j] != 0:
                # try check straight down
                try:
                    product = grid_int[i][j] * grid_int[i][j + 1] * grid_int[i][j + 2] * grid_int[i][j + 3]
                    if product > max_product:
                        max_product = product
                except:
                    continue
                
                # try check horizontal right
                try:
                    product = grid_int[i][j] * grid_int[i + 1][j] * grid_int[i + 2][j] * grid_int[i + 3][j]
                    if product > max_product:
                        max_product = product
                except:
                    continue
                
                # try check diagonal down right
                try:
                    product = grid_int[i][j] * grid_int[i + 1][j + 1] * grid_int[i + 2][j + 2] * grid_int[i + 3][j + 3]
                    if product > max_product:
                        max_product = product
                except:
                    continue
            
                # try check diagonal up right
                try:
                    product = grid_int[i][j] * grid_int[i + 1][j - 1] * grid_int[i + 2][j - 2] * grid_int[i + 3][j - 3]
                    if product > max_product:
                        max_product = product
                except:
                    continue
    
    if max_product == 0:
        log_msg("error", "Could not find max product.")
        return -1
    else:
        log_msg("result", "Max product: {}".format(max_product))
        return max_product
    
    # grid_int_reduced_int = [[str(int(x)).zfill(2) if str(x) != '0' else '  ' for x in grid_line] for grid_line in grid_int_reduced]
    
    # non_zero_count = [[1 for x in grid_line if x > 0] for grid_line in grid_int_reduced]
    # non_zero_count = sum([sum(grid_line) for grid_line in non_zero_count])
    # grid_average = sum([sum(grid_line) for grid_line in grid_int_reduced]) / non_zero_count
    # grid_int_reduced = [[x - grid_average if x - grid_average > 0 else 0 for x in grid_line] for grid_line in grid_int_reduced] 

        
if __name__ == "__main__":
    log_msg("info", "Starting processing of Problem 11")
    start_time = time.time()
    main()
    end_time = time.time() - start_time
    log_msg("info", "Time taken to run main function: {} seconds".format(end_time))
                            