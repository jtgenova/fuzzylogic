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
from interval import interval
import pymatrices as pm
import ece6397_genova_helper_headerfooter as header_footer

def inverse(size, mat, inv):
    """
    Find the inverse using adjoint/determinant.
    """
    # Find adjoint for inverse
    adj = pm.adjoint(mat)
    # print(f'Adjoint of the product: {adj}')
    # Find determinant for inverse
    det = pm.determinant(mat)
    # dividing by determinant doesn't work so fix manually
    det_rec = interval([1/det[0][1] , 1/det[0][0]])
    # print(f'Determinant of the product: {det_rec}')

    # Find inverse
    for i in range(size):
        for j in range(size):
            inv[i][j] = interval.__rmul__(adj[i][j] , det_rec)

    return inv

def data_est(count, u_vec, y_vec):
    """
    Create A matrix
    Find A transpose
    Find A.T*A
    Find inv(A.T*A)
    Find x
    Find b_hat
    """
    u_k_int = [[] for i in range(len(count))]
    y_k_int = [[] for i in range(len(count))]
    zero_int = interval([0,0])

    for i in range(len(count)):
        u_k_int[i] = interval(u_vec[i])
        y_k_int[i] = interval(y_vec[i])
    print('y(k) = -d1*y(k-1)  - d2*y(k-2) - d3*y(k-3)  - n0*u(k) - n1*u(k-1) - n2*u(k-2)')
    # create A matrix
    a_mat = pm.matrix([[-y_k_int[0], zero_int, zero_int,  u_k_int[1], u_k_int[0], zero_int],
                       [-y_k_int[1], -y_k_int[0],  zero_int,  u_k_int[2], u_k_int[1], u_k_int[0]],
                       [-y_k_int[2], -y_k_int[1], -y_k_int[0], u_k_int[3], u_k_int[2], u_k_int[1]],
                       [-y_k_int[3], -y_k_int[2], -y_k_int[1], u_k_int[4], u_k_int[3], u_k_int[2]],
                       [-y_k_int[4], -y_k_int[3], -y_k_int[2], u_k_int[5], u_k_int[4], u_k_int[3]],
                       [-y_k_int[5], -y_k_int[4], -y_k_int[3], u_k_int[6], u_k_int[5], u_k_int[4]],
                       [-y_k_int[6], -y_k_int[5], -y_k_int[4], u_k_int[7], u_k_int[6], u_k_int[5]]])
    print(f'A matrix: {a_mat}\n')
    # create b vector
    b_vec = pm.matrix([[y_k_int[1]],
                       [y_k_int[2]],
                       [y_k_int[3]],
                       [y_k_int[4]],
                       [y_k_int[5]],
                       [y_k_int[6]],
                       [y_k_int[7]]])
    print(f'b vector: {b_vec}')
    # transpose A matrix
    a_trans = a_mat.transpose
    # print(f'A^T matrix: {a_trans}')
    a_prod = interval.__rmul__(a_trans , a_mat)
    # print(f'A^T(A) matrix: {a_prod}')

    inv = [None for k in range(len(a_prod[0]))]
    for i in range(len(a_prod[0])):
        inv[i] = [None for k in range(len(a_prod[0]))]
    # find inverse
    a_prod_inv = pm.matrix(inverse(len(a_prod[0]) , a_prod , inv))
    # print(f'Inverse of the product: {a_prod_inv}')

    # Find x
    x_vec = interval.__rmul__(interval.__rmul__(a_prod_inv , a_trans) , b_vec)
    # print(f'x: {x}')
    print("Questions:")
    print('1. Using all of the measurements, calculate the parameters di and nj.')
    print(f'd1= {x_vec[0]}')
    print(f'd2= {x_vec[1]}')
    print(f'd3 = {x_vec[2]}')
    print(f'n0 = {x_vec[3]}')
    print(f'n1 = {x_vec[4]}')
    print(f'n2 = {x_vec[5]}\n')

    b_hat = interval.__rmul__(a_mat , x_vec)
    print('2. Using the parameters from [A] calculate ˆb.')
    print(f'b_hat = {b_hat}')

    print('3. Determine if b ⊆ ˆb or ˆb ⊆ b')
    print('b ⊆ ˆb')
    print('intervals in b are much smaller than intervals in ˆb')
##################################################################################################
if __name__=="__main__":
    CA_NUM = 5
    DESCRIPTION = "Perform the following sampled data estimations for a system with interval I/O."
    header_footer.header(CA_NUM, DESCRIPTION)
    start_time = time.time()
    k = list(range(8))
    u_k = [[1,3], [2,3], [3,4], [4,6], [4,5], [4,4.5], [5,5.5], [5,6]]
    y_k = [[1,2], [2,3], [2,3.5], [2.25,4], [2,3.5], [1.25,2], [1.5,2], [2,2.25]]
    print(f'u(k): {u_k}')
    print(f'y(k): {y_k}\n')
    data_est(k, u_k, y_k)
    final_time = time.time() - start_time
    header_footer.footer(final_time)
