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
import sys
from interval import interval
import ece6397_genova_helper_headerfooter as header_footer