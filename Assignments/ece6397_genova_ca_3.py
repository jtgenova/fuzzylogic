"""
ECE 6397: Fuzzy Logic
Professor: Dr. Steven Provence
Author: Joshua Genova
Computer Assignment #3
Description: Given a plain text file that contains the name of a set in the first line and the members of the set in the following lines, calculate the Power Set of the set.
             Display the results in the body of the output --the empty set can be either Ø or set(). After all of the members of the power set are displayed, print the number of the members of the Power Set.
             The script should be capable of reading in any text file of the same format and calculting a given Power Set.
Deadline: February 10, 2023 11:59PM
"""
import time
import ece6397_genova_helper_headerfooter as header_footer
import os
import sys
from itertools import chain, combinations


def power_set(text_file):
    with open(text_file) as f:
        lines = f.readlines()

    new_list = list(lines[1:len(lines)])
    print(f'Set {lines[0]}')
    total_members = len(new_list)
    res = []
    for sub in new_list:
        res.append(sub.replace("\n", ""))

    while("" in res):
        res.remove("")
    total_members = len(res)
    new_set = list(chain.from_iterable(combinations(res, r) for r in range(len(res)+1)))
    for i in range(len(new_set)):
        print(new_set[i])
    print(f'Number of members of Power Set: {2**total_members}')
    print(f'Number of members of Power Set: {len(new_set)}')
##################################################################################################
if __name__=="__main__":
    CA_NUM = 3
    DESCRIPTION = "Given a plain text file that contains the name of a set in the first line and the members of the set in the following lines, calculate the Power Set of the set."
    header_footer.header(CA_NUM, DESCRIPTION)
    ROOT = os.getcwd() + '\Assignments'
    # filename = ROOT + '\Set_for_CA3.txt'
    filename = sys.argv[1]
    power_set(filename)
    start_time = time.time()
    final_time = time.time() - start_time
    header_footer.footer(final_time)