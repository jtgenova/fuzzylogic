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
from matplotlib import pyplot as plt
import ece6397_genova_helper_headerfooter as header_footer

def calc_vals(set_range, start_zero, mid_one, end_zero):
    slope1 = 1/(mid_one - start_zero)
    b1 = -slope1*start_zero
    slope2 = -1/(end_zero - mid_one)
    b2 = -slope2*end_zero
    # print(f'slope1 = {slope1}, b1 = {b1}')
    # print(f'slope2 = {slope2}, b2 = {b2}')

def add_fuzzy(a, mf_a, b, mf_b):
    c_add, mf_cadd = fuzzy_add(a, mf_a, b, mf_b)

    plt.figure(figsize=(15,5))
    plt.subplot(1,3,1)
    plt.xlim([0, 20])
    plt.plot(a, mf_a)
    plt.xlabel("a", fontdict={'family':'serif','color':'darkred','size':10})
    plt.ylabel(r'$u_{A}(a)$', fontdict={'family':'serif','color':'darkred','size':10})
    plt.title("Set A", fontdict ={'family':'serif','color':'blue','size':12})

    plt.subplot(1,3,2)
    plt.xlim([0, 20])
    plt.plot(b, mf_b)
    plt.xlabel("b", fontdict={'family':'serif','color':'darkred','size':10})
    plt.ylabel(r'$u_{B}(b)$', fontdict={'family':'serif','color':'darkred','size':10})
    plt.title("Set B", fontdict ={'family':'serif','color':'blue','size':12})

    plt.subplot(1,3,3)
    plt.xlim([0, 20])
    plt.plot(c_add, mf_cadd)
    plt.xlabel("c", fontdict={'family':'serif','color':'darkred','size':10})
    plt.ylabel(r'$u_{C}(c)$', fontdict={'family':'serif','color':'darkred','size':10})
    plt.title("A+B=C", fontdict ={'family':'serif','color':'blue','size':12})
    
    # plt.show(block=False)

def subtract_fuzzy(a, mf_a, b, mf_b):
    c_sub, mf_csub = fuzzy_sub(a, mf_a, b, mf_b)

    plt.figure(figsize=(15,5))
    plt.subplot(1,3,1)
    plt.xlim([-5, 13])
    plt.plot(a, mf_a)
    plt.xlabel("a", fontdict={'family':'serif','color':'darkred','size':10})
    plt.ylabel(r'$u_{A}(a)$', fontdict={'family':'serif','color':'darkred','size':10})
    plt.title("Set A", fontdict ={'family':'serif','color':'blue','size':12})

    plt.subplot(1,3,2)
    plt.xlim([-5, 13])
    plt.plot(b, mf_b)
    plt.xlabel("b", fontdict={'family':'serif','color':'darkred','size':10})
    plt.ylabel(r'$u_{B}(b)$', fontdict={'family':'serif','color':'darkred','size':10})
    plt.title("Set B", fontdict ={'family':'serif','color':'blue','size':12})

    plt.subplot(1,3,3)
    plt.xlim([-5, 13])
    plt.plot(c_sub, mf_csub)
    plt.xlabel("c", fontdict={'family':'serif','color':'darkred','size':10})
    plt.ylabel(r'$u_{C}(c)$', fontdict={'family':'serif','color':'darkred','size':10})
    plt.title("A-B=C", fontdict ={'family':'serif','color':'blue','size':12})
    
    # plt.show(block=False)

def multiply_fuzzy(a, mf_a, b, mf_b):
    c_mult, mf_cmult = fuzzy_mult(a, mf_a, b, mf_b)

    plt.figure(figsize=(15,5))
    plt.subplot(1,3,1)
    plt.xlim([0, 65])
    plt.plot(a, mf_a)
    plt.xlabel("a", fontdict={'family':'serif','color':'darkred','size':10})
    plt.ylabel(r'$u_{A}(a)$', fontdict={'family':'serif','color':'darkred','size':10})
    plt.title("Set A", fontdict ={'family':'serif','color':'blue','size':12})

    plt.subplot(1,3,2)
    plt.xlim([0, 65])
    plt.plot(b, mf_b)
    plt.xlabel("b", fontdict={'family':'serif','color':'darkred','size':10})
    plt.ylabel(r'$u_{B}(b)$', fontdict={'family':'serif','color':'darkred','size':10})
    plt.title("Set B", fontdict ={'family':'serif','color':'blue','size':12})

    plt.subplot(1,3,3)
    plt.xlim([0, 65])
    plt.plot(c_mult, mf_cmult)
    plt.xlabel("c", fontdict={'family':'serif','color':'darkred','size':10})
    plt.ylabel(r'$u_{C}(c)$', fontdict={'family':'serif','color':'darkred','size':10})
    plt.title("A*B=C", fontdict ={'family':'serif','color':'blue','size':12})
    
    # plt.show(block=False)


##################################################################################################
if __name__=="__main__":
    CA_NUM = 6
    DESCRIPTION = "Find the results of fuzzy triangular membership function arithmetic."
    header_footer.header(CA_NUM, DESCRIPTION)
    start_time = time.time()
    range_a = np.r_[1:12+1]
    a_vals = np.r_[0, 0, 0, 0, 0.5, 1, 0.8, 0.6, 0.4, 0.2, 0, 0]
    range_b = np.r_[2:5+1]
    b_vals = np.r_[0, 0, 1, 0]
    calc_vals(range_a, 4, 6, 11)
    add_fuzzy(range_a, a_vals, range_b, b_vals)
    subtract_fuzzy(range_a, a_vals, range_b, b_vals)
    multiply_fuzzy(range_a, a_vals, range_b, b_vals)
    final_time = time.time() - start_time
    header_footer.footer(final_time)
    plt.show()
