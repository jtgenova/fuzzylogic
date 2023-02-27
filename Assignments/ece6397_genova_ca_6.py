"""
ECE 6397: Fuzzy Logic
Professor: Dr. Steven Provence
Author: Joshua Genova
Computer Assignment #6
Description: 
    Given:
    A = [1,12] and a fuzzy triangular membership function: (0 at 4), (1 at 6), (0 at 11)
    B = [2,5] and a fuzzy triangular membership function: (0 at 3), (1 at 4), (0 at 5).
    Find:
    1. A+B
    2. A-B
    3. A*B
    The output should
    1) Display to the terminal the set results,
    additionally,
    2) a figure in seperate window should appear with a title of the operation
        and three subfigures of 
        a) fuzzy membership a, 
        b) fuzzy membership b, 
        c) the resulting fuzzy operation.
Deadline: March 5, 2023 11:59PM
"""
import time
from interval import interval
from skfuzzy.fuzzymath import fuzzy_add, fuzzy_sub, fuzzy_mult
import numpy as np
import ece6397_genova_helper_headerfooter as header_footer

def calc_vals(set_range, start_zero, mid_one, end_zero):
    slope1 = 1/(mid_one - start_zero)
    b1 = slope1*start_zero
    slope2 = -1/(end_zero - mid_one)
    b2 = slope2*end_zero
    
    
    return 

##################################################################################################
if __name__=="__main__":
    CA_NUM = 6
    DESCRIPTION = "Find the results of fuzzy triangular membership function arithmetic."
    header_footer.header(CA_NUM, DESCRIPTION)
    start_time = time.time()
    range_a = np.r_[1:12+1]
    range_b = np.r_[2:5+1]
    final_time = time.time() - start_time