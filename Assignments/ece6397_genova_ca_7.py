"""
ECE 6397: Fuzzy Logic
Professor: Dr. Steven Provence
Author: Joshua Genova
Computer Assignment #7
Description:
Write a script that performs the operations presented in class.
It should take in three arguments:
    1) n for a
    2) n for b
    3) a string sequence that determines the operations performed.
Deadline: April 2, 2023 11:59PM
"""

import time
import sys
import numpy as np
import ece6397_genova_helper_headerfooter as header_footer

def fix_string(form):
    """
    Fix inputs to remove any spacing.
    Put in an array.
    """
    size = len(form)
    string_list = []
    for i in range(size):
        string = form[i].replace("'", "")
        string_list.append(string)
    return string_list

def check_form(form):
    """
    Check which formula is used and put in an array.
    """
    new_form = fix_string(form)
    form_size = len(form)
    form_arr = np.zeros(6)
    for i in range(form_size):
        if new_form[i] == 'a':
            form_arr[0] = 1
        if new_form[i] == 'b':
            form_arr[1] = 1
        if new_form[i] == 'c':
            form_arr[2] = 1
        if new_form[i] == 'd':
            form_arr[3] = 1
        if new_form[i] == 'e':
            form_arr[4] = 1
        if new_form[i] == 'f':
            form_arr[5] = 1
    return form_arr

def create_set(size):
    """
    Create an array for size of set.
    """
    set_n = np.arange(0, 1+1/size, 1/size).tolist()
    return set_n

def form_a(a_var, b_var):
    """
    Formula a.
    """
    return float(min(a_var, b_var))

def form_b(a_var, b_var):
    """
    Formula b.
    """
    return float(a_var * b_var)

def form_c(a_var, b_var):
    """
    Formula c.
    """
    return float(min(1, 1+b_var-a_var))

def form_d(a_var, b_var):
    """
    Formula d.
    """
    return float(max(min(a_var, b_var), 1-a_var))

def form_e(a_var, b_var):
    """
    Formula e.
    """
    return float(max(1-a_var, b_var))

def form_f(a_var, b_var):
    """
    Formula f.
    """
    if a_var <= b_var:
        ans = float(1)
    if a_var > b_var:
        ans = float(b_var/a_var)
    return ans
def implication(a_var, b_var, formula):
    """
    Apply implication formula depending on input.
    """
    form = check_form(formula)
    a_set = create_set(a_var)
    b_set = create_set(b_var)
    a_set_size = len(a_set)
    b_set_size = len(b_set)
    for i in range(a_set_size):
        for j in range(b_set_size):
            if form[0] == 1:
                print(f'{a_set[i]:.5} => {b_set[j]:.5} = {form_a(a_set[i], b_set[j]):.5},        a')
            if form[1] == 1:
                print(f'{a_set[i]:.5} => {b_set[j]:.5} = {form_b(a_set[i], b_set[j]):.5},        b')
            if form[2] == 1:
                print(f'{a_set[i]:.5} => {b_set[j]:.5} = {form_c(a_set[i], b_set[j]):.5},        c')
            if form[3] == 1:
                print(f'{a_set[i]:.5} => {b_set[j]:.5} = {form_d(a_set[i], b_set[j]):.5},        d')
            if form[4] == 1:
                print(f'{a_set[i]:.5} => {b_set[j]:.5} = {form_e(a_set[i], b_set[j]):.5},        e')
            if form[5] == 1:
                print(f'{a_set[i]:.5} => {b_set[j]:.5} = {form_f(a_set[i], b_set[j]):.5},        f')
            print('\n')
##################################################################################################
if __name__=="__main__":
    CA_NUM = 7
    DESCRIPTION = "Write a script that performs the operations presented in class."
    header_footer.header(CA_NUM, DESCRIPTION)
    start_time = time.time()
    N = int(sys.argv[1])
    M = int(sys.argv[2])
    FORMULA = sys.argv[3:]
    implication(M, N, FORMULA)
    final_time = time.time() - start_time
    header_footer.footer(final_time)
