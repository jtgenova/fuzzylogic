"""
ECE 6397: Fuzzy Logic
Professor: Dr. Steven Provence
Author: Joshua Genova
Description: Header and Footer for all assignments
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
    if time_elapsed >= 1:
        print(f'Run time: {time_elapsed:.5} s')
    if time_elapsed < 1 and time_elapsed >= 0.001:
            print(f'Run time: {time_elapsed*1000:.5} ms')
    if time_elapsed < 0.001:
        print(f'Run time: {time_elapsed*1000000:.5} \u03BCs')
    print('END RUN')

if __name__=="__main__":
    header(1, "Using python 3.8, calculate the first nine integers of the Fibonacci sequence.")
    start_time = time.time()
    for i in range(1000):
        pass
    final_time = time.time() - start_time
    print(final_time)
    footer(final_time)
