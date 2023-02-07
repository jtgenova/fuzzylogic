"""
ECE 6397: Fuzzy Logic
Professor: Dr. Steven Provence
Author: Joshua Genova
Computer Assignment #3
Description: Given a plain text file that contains the name
             of a set in the first line and the members of
             the set in the following lines, calculate the Power Set of the set.
             Display the results in the body of the output
             --the empty set can be either Ø or set().
             After all of the members of the power set are displayed,
             print the number of the members of the Power Set.
             The script should be capable of reading in any text file
             of the same format and calculting a given Power Set.
Deadline: February 10, 2023 11:59PM
"""
import time
import sys
from itertools import chain, combinations
from ast import literal_eval
import ece6397_genova_helper_headerfooter as header_footer


def power_set(text_file):
    """
    Create power set list from given set list from a text file.
    """
    with open(text_file, encoding='utf-8') as input_file:
        lines = input_file.readlines()

    # remove \n
    rm_new_line = []
    for sub in lines:
        rm_new_line.append(sub.replace("\n", ""))
    # remove empty
    while "" in rm_new_line:
        rm_new_line.remove("")
    # create new set
    new_set = list(rm_new_line[1:len(rm_new_line)])
    new_set = [literal_eval(i) for i in new_set]
    print(f'Set {rm_new_line[0]}: {new_set}')
    # print(f'Number of members of Power Set: {2**len(set)}')
    return list(chain.from_iterable(combinations(new_set, r) for r in range(len(new_set)+1)))
##################################################################################################
if __name__=="__main__":
    CA_NUM = 3
    DESCRIPTION = "Given a plain text file, calculate the Power Set of the set."
    header_footer.header(CA_NUM, DESCRIPTION)
    start_time = time.time()
    FILENAME = sys.argv[1]
    list_power_set = power_set(FILENAME)
    MAXIDX = len(list_power_set)
    for i in range(MAXIDX):
        print(list_power_set[i])
    print(f'Number of members of Power Set: {len(list_power_set)}')
    final_time = time.time() - start_time
    header_footer.footer(final_time)
