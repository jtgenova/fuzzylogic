"""
ECE 6397: Fuzzy Logic
Professor: Dr. Steven Provence
Author: Joshua Genova
Computer Assignment #4
Description: Use the intererval module to perform all of the  interval arithmatic 
             operations (+, -, * ,/ , min ,max) on A = [2, 14] and B = [1, 16].
             Namely, A+B, A-B, A*B, A/B, min(A,B), max(A,B).
             The output should be clear and easily read by someone unfamilar 
            to set theory and interval arithmatic. 
Deadline: February 18, 2023 11:59PM
"""
import time
from interval import interval
import ece6397_genova_helper_headerfooter as header_footer

def add(a_int, b_int):
    """
    Adding intervals.
    """
    return a_int + b_int

def subtract(a_int, b_int):
    """
    Subtracting intervals.
    """
    return a_int - b_int

def multiply(a_int, b_int):
    """
    Multiplying intervals.
    """
    return a_int * b_int

def divide(a_int, b_int):
    """
    Dividing intervals.
    """
    return a_int / b_int

def min_interval(a_int, b_int):
    """
    Find min of intervals.
    """
    min_min = min(a_int[0], b_int[0])
    min_max = min(a_int[1], b_int[1])
    return interval([min_min, min_max])

def max_interval(a_int, b_int):
    """
    Find max of intervals.
    """
    max_min = max(a_int[0], b_int[0])
    max_max = max(a_int[1], b_int[1])
    return interval([max_min, max_max])
##################################################################################################
if __name__=="__main__":
    CA_NUM = 4
    DESCRIPTION = "Use the intererval module to perform all of the  interval arithmetic operations."
    header_footer.header(CA_NUM, DESCRIPTION)
    start_time = time.time()
    A = [2, 14]
    B = [1, 16]
    print(f'Interval A = {A}')
    print(f'Interval B = {B}')
    A_interval = interval(A)
    B_interval = interval (B)
    print(f'A + B = {add(A_interval,B_interval)}')
    print(f'A - B = {subtract(A_interval,B_interval)}')
    print(f'A * B = {multiply(A_interval,B_interval)}')
    print(f'A / B = {divide(A_interval,B_interval)}')
    print(f'max(A,B) = {max_interval(A,B)}')
    print(f'min(A,B) = {min_interval(A,B)}')

    final_time = time.time() - start_time
    header_footer.footer(final_time)
    