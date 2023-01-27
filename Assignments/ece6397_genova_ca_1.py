"""
ECE 6397: Fuzzy Logic
Professor: Dr. Steven Provence
Author: Joshua Genova
Computer Assignment #1
Description: Using python 3.8, calculate the first nine integers of the Fibonacci sequence.
Deadline: January 28, 2023 11:59PM
"""
import time
import ece6397_Genova_helperHeaderFooter as header_footer


def fibonacci_sequence(num_seq):
    """
    Printing Fibonnaci Sequence.
    """

    fib_num = [0, 1]
    print(f"Sequence 1 is {fib_num[0]}\n")
    print(f"Sequence 2 is {fib_num[1]}\n")
    for i in range(2, num_seq):
        fib_num.append(fib_num[i-1]+fib_num[i-2])
        print(f"Sequence {i+1} is {fib_num[i]}\n")
##################################################################################################
if __name__=="__main__":
    CA_NUM = 1
    DESCRIPTION = "Calculate the first nine integers of the Fibonacci Sequence."
    header_footer.header(CA_NUM, DESCRIPTION)
    start_time = time.time()
    fibonacci_sequence(9)
    final_time = time.time() - start_time
    header_footer.footer(final_time)
