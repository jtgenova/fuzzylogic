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

def distributive_laws(S, A, B, C):
    """
    Printing and verifying the distributive laws.
    """
    A_not = S-A
    B_not = S-B
    C_not = S-C
    E = set([])
    print(f'The Universe Set S is {S}')
    print(f'The Subset A is {A}')
    print(f'The Subset B S is {B}')
    print(f'The Subset C S is {C}\n')
    ##################################################################################
    print(f'A cap (B cup C): {A & (B | C)}')
    print(f'(A cap B) cup (A cap C): {(A & B) | (A & C)}')
    print(f'A cup (B cap C): {A | (B & C)}')
    print(f'(A cup B) cap (A cup C): {(A | B) & (A| C)}')
    print(f'A cup A: {A | A}')
    print(f'A cap A: {A & A}')
    print(f'A cup (A cap B): {A | (A & B)}')
    print(f'A cap (A cup B): {A & (A | B)}')
    print(f'A cup (A complement cap B): {A | (A_not & B)}')
    print(f'A cup B: {A | B}')
    print(f'A cap (A complement cup B): {A & (A_not | B)}')
    print(f'A cap B: {A & B}')
    print(f'A cup S: {A | S}')
    print(f'A cap Empty: {A & E}')
    print(f'A cup Empty: {A | E}')
    print(f'A cap S: {A & S}')
    print(f'A cap A complement: {A & A_not}')
    print(f'A cup A complement: {A | A_not}')



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
