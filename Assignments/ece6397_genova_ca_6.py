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
from skfuzzy.fuzzymath import fuzzy_add, fuzzy_sub, fuzzy_mult
from skfuzzy.membership import trimf
import numpy as np
from matplotlib import pyplot as plt
import math
import ece6397_genova_helper_headerfooter as header_footer

def add_fuzzy(a_set, mf_a, b_set, mf_b):
    """
    use fuzzy_add to add two sets and print the results.
    """
    c_add, mf_cadd = fuzzy_add(a_set, mf_a, b_set, mf_b)

    plt.figure(figsize=(15,5))
    plt.subplot(1,3,1)
    plt.xlim([0, 20])
    plt.plot(a_set, mf_a)
    plt.xlabel("a", fontdict={'family':'serif','color':'darkred','size':10})
    plt.ylabel(r'$u_{A}(a)$', fontdict={'family':'serif','color':'darkred','size':10})
    plt.title("Set A", fontdict ={'family':'serif','color':'blue','size':12})

    plt.subplot(1,3,2)
    plt.xlim([0, 20])
    plt.plot(b_set, mf_b)
    plt.xlabel("b", fontdict={'family':'serif','color':'darkred','size':10})
    plt.ylabel(r'$u_{B}(b)$', fontdict={'family':'serif','color':'darkred','size':10})
    plt.title("Set B", fontdict ={'family':'serif','color':'blue','size':12})

    plt.subplot(1,3,3)
    plt.xlim([0, 20])
    plt.plot(c_add, mf_cadd)
    plt.xlabel("c", fontdict={'family':'serif','color':'darkred','size':10})
    plt.ylabel(r'$u_{C}(c)$', fontdict={'family':'serif','color':'darkred','size':10})
    plt.title("A+B=C", fontdict ={'family':'serif','color':'blue','size':12})
    return c_add, mf_cadd

def subtract_fuzzy(a_set, mf_a, b_set, mf_b):
    """
    use fuzzy_sub to subtract sets and print the results.
    """
    c_sub, mf_csub = fuzzy_sub(a_set, mf_a, b_set, mf_b)

    plt.figure(figsize=(15,5))
    plt.subplot(1,3,1)
    plt.xlim([-5, 13])
    plt.plot(a_set, mf_a)
    plt.xlabel("a", fontdict={'family':'serif','color':'darkred','size':10})
    plt.ylabel(r'$u_{A}(a)$', fontdict={'family':'serif','color':'darkred','size':10})
    plt.title("Set A", fontdict ={'family':'serif','color':'blue','size':12})

    plt.subplot(1,3,2)
    plt.xlim([-5, 13])
    plt.plot(b_set, mf_b)
    plt.xlabel("b", fontdict={'family':'serif','color':'darkred','size':10})
    plt.ylabel(r'$u_{B}(b)$', fontdict={'family':'serif','color':'darkred','size':10})
    plt.title("Set B", fontdict ={'family':'serif','color':'blue','size':12})

    plt.subplot(1,3,3)
    plt.xlim([-5, 13])
    plt.plot(c_sub, mf_csub)
    plt.xlabel("c", fontdict={'family':'serif','color':'darkred','size':10})
    plt.ylabel(r'$u_{C}(c)$', fontdict={'family':'serif','color':'darkred','size':10})
    plt.title("A-B=C", fontdict ={'family':'serif','color':'blue','size':12})
    return c_sub, mf_csub

def multiply_fuzzy(a_set, mf_a, b_set, mf_b):
    """
    use fuzzy_mult to multiply sets and print the results.
    """
    # method 1
    c_mult, mf_cmult = fuzzy_mult(a_set, mf_a, b_set, mf_b)

    # method 2
    c_set = np.r_[c_mult[0] : c_mult[len(c_mult)-1]+1]
    c_uf = trimf(c_set, [12, 24, 55])

    # method 3
    c_hand = np.zeros(len(c_set))
    for i in range(12-2, 24-1):
        c_hand[i] = (-10 + math.sqrt(10**2 - 4*2*(12-c_set[i])))/(2*2)
        # print(f'{c_set[i]}: {c_hand[i]}')
    for i in range(25-2, 55-1):
        c_hand[i] = (36 - math.sqrt((-36)**2 - 4*5*(55-c_set[i])))/(2*5)
        # print(f'{c_set[i]}: {c_hand[i]}')

    plt.figure(figsize=(15,5))
    plt.subplot(1,3,1)
    plt.xlim([0, 65])
    plt.plot(a_set, mf_a)
    plt.xlabel("a", fontdict={'family':'serif','color':'darkred','size':10})
    plt.ylabel(r'$u_{A}(a)$', fontdict={'family':'serif','color':'darkred','size':10})
    plt.title("Set A", fontdict ={'family':'serif','color':'blue','size':12})

    plt.subplot(1,3,2)
    plt.xlim([0, 65])
    plt.plot(b_set, mf_b)
    plt.xlabel("b", fontdict={'family':'serif','color':'darkred','size':10})
    plt.ylabel(r'$u_{B}(b)$', fontdict={'family':'serif','color':'darkred','size':10})
    plt.title("Set B", fontdict ={'family':'serif','color':'blue','size':12})

    plt.subplot(1,3,3)
    plt.xlim([0, 65])
    plt.plot(c_mult, mf_cmult, label='fuzzy_mult')
    plt.xlabel("c", fontdict={'family':'serif','color':'darkred','size':10})
    plt.ylabel(r'$u_{C}(c)$', fontdict={'family':'serif','color':'darkred','size':10})
    plt.title("A*B=C", fontdict ={'family':'serif','color':'blue','size':12})

    plt.plot(c_set, c_uf, label='approximation')

    plt.plot(c_set, c_hand, label='work by hand')

    return c_set, c_hand
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
    print('Given:')
    print(f'Set A = {range_a}')
    print(f'Set B = {range_b}\n')
    sum_c, sum_mfc = add_fuzzy(range_a, a_vals, range_b, b_vals)
    print('1. A + B = C')
    print(f'C = {sum_c}')
    print(f'\u03BC(c) = {sum_mfc}\n')

    diff_c, diff_mfc = subtract_fuzzy(range_a, a_vals, range_b, b_vals)
    print('2. A - B = C')
    print(f'C = {diff_c}')
    print(f'\u03BC(c) = {diff_mfc}\n')

    prod_c, prod_mfc = multiply_fuzzy(range_a, a_vals, range_b, b_vals)
    print('3. A * B = C')
    print(f'C = {prod_c}')
    print(f'\u03BC(c) = {prod_mfc}')
    plt.show(block=False)
    final_time = time.time() - start_time
    header_footer.footer(final_time)
    plt.legend()
    plt.show()
    