"""
ECE 6397: Fuzzy Logic
Professor: Dr. Steven Provence
Author: Joshua Genova
Computer Assignment #1
Description: Using python 3.8, calculate the first nine integers of the Fibonacci sequence.
Deadline: January 28, 2023 11:59PM
"""
import time

def header(assignment_number, description):
    """
    Header for assignment per instructions.
    """

    print('-'*79)
    print('-'*79)
    print('Last: Genova')
    print('First: Joshua')
    print(f"Computer Assignment: {assignment_number}")
    print('-'*79)
    print(f"Description: {description}")
    print('START RUN')
    print('-'*79)

def footer(time_elapsed):
    """
    Footer for assignment per instructions.
    Need time elapsed.
    """

    print('-'*79)
    print(f'Run time: {time_elapsed:.5f}s')
    print('END RUN')

def fibonacci_sequence(num_seq):
    """
    Printing Fibonnaci Sequence.
    """

    fib_num = [0, 1]
    for i in range(2, num_seq):
        fib_num.append(fib_num[i-1]+fib_num[i-2])
    for _ in range(num_seq):
        print(f"Sequence {_+1} is {fib_num[_]}")


if __name__=="__main__":
    header(1,"Using python 3.8, calculate the first nine integers of the Fibonacci sequence.")
    start_time = time.time()
    fibonacci_sequence(9)
    final_time = time.time() - start_time
    footer(final_time)
