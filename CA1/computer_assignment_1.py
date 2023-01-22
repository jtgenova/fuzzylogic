#  -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------
# Genova
# Joshua
# Computer Assignment: 1
# -------------------------------------------------------------------------------
"""Description: Using python 3.8, calculate the first nine integers of the Fibonacci sequence."""
# START RUN
# -------------------------------------------------------------------------------

import time
start_time = time.time()

N1 = 0
N2 = 1
NUMSEQ = 9
for i in range(NUMSEQ):
    NCURRENT = N1 + N2
    if i == 0:
        NCURRENT = 0
    if i == 1:
        NCURRENT = 1
    print(f"Sequence {i+1} is {NCURRENT}")
    N1 = N2
    N2 = NCURRENT

print(f"Process finished --- {time.time() - start_time} seconds ---")

# -------------------------------------------------------------------------------
# Run time: ~0.003 seconds
# END RUN
