"""
ECE 6397: Fuzzy Logic
Professor: Dr. Steven Provence
Author: Joshua Genova
Computer Assignment #5
Description: Perform the following sampled data estimations for a system with interval I/O. 
             The results should be clearly presented in the body of the code. present the results.
             - Using all of the measurements, calculate the parameters di and nj.
             - Using the parameters from [A] calculate ˆb.
             - Determine if b ⊆ ˆb or ˆb ⊆ b
Deadline: February 26, 2023 11:59PM
"""
import time
import ece6397_genova_helper_headerfooter as header_footer
import numpy as np
from interval import interval

def data_est(k, u_k, y_k):
    u_int =  np.zeros(shape=(8,1))
    y_int =  np.zeros(shape=(8,1))
    print(interval(u_k[0]))
    # change into intervals
    for i in range(8):
        u_int[i] = interval(u_k[i])
        y_int[i] = interval(y_k[i])
        
    rows = 8
    A_mat = np.array([-y_k[0], 0, u_k[0], 0])
    # A_mat = np.zeros(shape=(rows,4))
    # A_mat[0] = [-y_k[0], 0, u_k[0], 0]
    print(A_mat)
    # idx = 0
    # for i in range(0, rows, 2):
    #     l_mat[i] = xf[idx]
    #     l_mat[i+1] = yf[idx]
    #     idx += 1
    return

##################################################################################################
if __name__=="__main__":
    CA_NUM = 5
    DESCRIPTION = "Perform the following sampled data estimations for a system with interval I/O."
    header_footer.header(CA_NUM, DESCRIPTION)
    start_time = time.time()
    k = list(range(8))
    u_k = np.array([[1,3], [2,3], [3,4], [4,6], [4,5], [4,4.5], [5,5.5], [5,6]])
    y_k = np.array([[1,2], [2,3], [2,3.5], [2.25,4], [2,3.5], [1.25,2], [1.5,2], [2,2.25]])
    data_est(k, u_k, y_k)
    final_time = time.time() - start_time
    header_footer.footer(final_time)