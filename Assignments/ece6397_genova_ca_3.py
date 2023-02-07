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
from itertools import chain, combinations


def power_set(text_file):
    # print(text_file)
    with open(text_file) as f:
        lines = f.readlines()

    s = list(lines[1:len(lines)])
    print(s)
    new_set = list(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))
    for i in range(len(new_set)):
        print(new_set[i])
##################################################################################################
if __name__=="__main__":
    CA_NUM = 3
    DESCRIPTION = "Given a plain text file that contains the name of a set in the first line and the members of the set in the following lines, calculate the Power Set of the set."
    header_footer.header(CA_NUM, DESCRIPTION)
    ROOT = os.getcwd() + '\Assignments'
    filename = ROOT + '\Set_for_CA3.txt'
    power_set(filename)
    start_time = time.time()
    final_time = time.time() - start_time
    header_footer.footer(final_time)