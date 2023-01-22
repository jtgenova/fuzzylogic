# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------
# Genova
# Joshua
# Computer Assignment: 1
# -------------------------------------------------------------------------------
# Description: Using python 3.8, calculate the first nine integers of the Fibonacci sequence.
# START RUN
# -------------------------------------------------------------------------------
import time
start_time = time.time()

n1 = 0
n2 = 1
num_seq = 9
for i in range(num_seq):
    n_current = n1 + n2
    if i == 0:
        n_current = 0
    if i == 1:
        n_current = 1
    print(f"Sequence {i+1} is {n_current}")
    n1 = n2
    n2 = n_current

print("Process finished --- %s seconds ---" % (time.time() - start_time))
# -------------------------------------------------------------------------------
# Run time: ~0.003 seconds
# END RUN