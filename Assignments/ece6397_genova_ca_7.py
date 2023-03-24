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
    string_list = []
    for i in range(len(form)):
        string = form[i].replace("'", "")
        string_list.append(string)
    return string_list

def check_form(form):
    new_form = fix_string(form)
    form_arr = np.zeros(5)
    for i in range(len(form)):
        if new_form[i] == 'b':
            form_arr[0] = 1
        if new_form[i] == 'c':
            form_arr[1] = 1
        if new_form[i] == 'd':
            form_arr[2] = 1
        if new_form[i] == 'e':
            form_arr[3] = 1
        if new_form[i] == 'f':
            form_arr[4] = 1
    return form_arr

def set(size):
    set_n = np.arange(0, 1+1/size, round(1/size, 3)).tolist()
    return set_n

def form_b(a, b):
    return a * b

def form_c(a, b):
    return min(1, 1+b-a)

def form_d(a, b):
    return max(min(a, b), 1-a)

def form_e(a, b):
    return max(1-a, b)

def form_f(a, b):
    if a <= b:
        return 1
    if a > b:
        return b/a

def implication(A, B, formula):
    form = check_form(formula)
    A = set(A)
    B = set(B)
    A_size = len(A)
    B_size = len(B)
    for i in range(A_size):
        for j in range(B_size):
            if form[0] == 1:
                print(f'{A[i]} => {B[j]} = {form_b(A[i], B[j])},        b')
            if form[1] == 1:
                print(f'{A[i]} => {B[j]} = {form_c(A[i], B[j])},        c')
            if form[2] == 1:
                print(f'{A[i]} => {B[j]} = {form_d(A[i], B[j])},        d')
            if form[3] == 1:
                print(f'{A[i]} => {B[j]} = {form_e(A[i], B[j])},        e')
            if form[4] == 1:
                print(f'{A[i]} => {B[j]} = {form_f(A[i], B[j])},        f')
            
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
    new_form = implication(M, N, FORMULA)
    final_time = time.time() - start_time
    header_footer.footer(final_time)
