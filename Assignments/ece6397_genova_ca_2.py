"""
ECE 6397: Fuzzy Logic
Professor: Dr. Steven Provence
Author: Joshua Genova
Computer Assignment #2
Description: Calculate and verify all of the Distributive Laws from the textbook table.
Deadline: February 4, 2023 11:59PM
"""
import time
import ece6397_genova_headerfooter as header_footer

def distributive_laws(s_uni, a_set, b_set, c_set):
    """
    Printing and verifying the distributive laws.
    """
    a_not = s_uni-a_set
    empty_set = set([])
    print(f'The Universe Set S is {s_uni}')
    print(f'The Subset A is {a_set}')
    print(f'The Subset B S is {b_set}')
    print(f'The Subset C S is {c_set}\n')
    ##################################################################################
    print('Distributive Law 1')
    print(f'A cap (B cup C): {a_set & (b_set | c_set)}')
    print(f'(A cap B) cup (A cap C): {(a_set & b_set) | (a_set & c_set)}\n')

    print('Distributive Law 2')
    print(f'A cup (B cap C): {a_set | (b_set & c_set)}')
    print(f'(A cup B) cap (A cup C): {(a_set | b_set) & (a_set| c_set)}\n')

    print('Distributive Law 3')
    print(f'A cup A: {a_set | a_set}\n')

    print('Distributive Law 4')
    print(f'A cap A: {a_set & a_set}\n')

    print('Distributive Law 5')
    print(f'A cup (A cap B): {a_set | (a_set & b_set)}\n')

    print('Distributive Law 6')
    print(f'A cap (A cup B): {a_set & (a_set | b_set)}\n')

    print('Distributive Law 7')
    print(f'A cup (A complement cap B): {a_set | (a_not & b_set)}')
    print(f'A cup B: {a_set | b_set}\n')

    print('Distributive Law 8')
    print(f'A cap (A complement cup B): {a_set & (a_not | b_set)}')
    print(f'A cap B: {a_set & b_set}\n')

    print('Distributive Law 9')
    print(f'A cup S: {a_set | s_uni}\n')

    print('Distributive Law 10')
    print(f'A cap Empty: {a_set & empty_set}\n')

    print('Distributive Law 11')
    print(f'A cup Empty: {a_set | empty_set}\n')

    print('Distributive Law 12')
    print(f'A cap S: {a_set & s_uni}\n')

    print('Distributive Law 13')
    print(f'A cap A complement: {a_set & a_not}\n')

    print('Distributive Law 14')
    print(f'A cup A complement: {a_set | a_not}')
##################################################################################################
if __name__=="__main__":
    CA_NUM = 2
    DESCRIPTION = "Calculate and verify all of the Distributive Laws from the textbook table."
    header_footer.header(CA_NUM, DESCRIPTION)
    start_time = time.time()
    S = set(list(range(1, 11)))
    A = set(list(range(2, 12, 2)))
    B = set(list(range(1,6)))
    C = set(list(range(5,11)))
    distributive_laws(S, A, B, C)
    final_time = time.time() - start_time
    header_footer.footer(final_time)
