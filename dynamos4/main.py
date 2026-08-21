#----------------------------------------------
# Recursion Practice Python
#
# Base Cases -> Stopping condition preventing infinite recursion
# Recursice Step -> Sub-problem reduction moving toward base case
# Call Stack Overhead: Stack Frame creation overhead in Python
# Call Stack Depth: Python default max recursion depth limit
#
# C++ -> Python considerations
# std::string ---> str
# double[] / float[] ---> list[float]
# int[] ---> list[int]
# Pass by reference (&) ---> Python object reference sementics
# std::chrono ---> time.perf_counter()
#-----------------------------------------------------

import time
import sys

#increasing the default recursion limit for perfromance benchmark execution
sys.setrecursionlimit(50000)

#-----------------------------------------------------------
# Functions 1: recursive function that receives an integer n
# as a parameter and calculates the 
# formula: 1 + 2×2 + 3 + 2×4 + 5 + 2×6 + ... up to n.
#-------------------------------------------------------------
# Recursive
# Should break into sub-problems: f(n) = term(n) + f(n - 1)
# Base case stops at n=0 returning 0

def series_sum_rec(n: int) -> int:
    if n <= 0:
        return 0
    term = (2 * n) if ( n % 2 == 0) else n
    return term + series_sum_rec(n - 1)

# Iterative
# -- Linear accumulation in a single frame is 0(1) space
def series_sum_iter(n: int) -> int:
    total = 0
    for i in range(1, n + 1):
        total += (2 * i) if (i % 2 == 0) else i
    return total


#------------------------------------------------------
# Functions 2: function that receives an
# integer n as a parameter and calculates the formula 
# (0 × 1) + (1 × 2) + (2 × 3) + (3 × 4) + ... (n-1)×n.
#-----------------------------------------------------------
# Recursive 
# Base case n <= 1 will yield 0. It evaluated term at n,
# then recurses on n -1
def product_series_rec(n: int) -> int:
    if n <= 1:
        return 0
    return (n - 1) * n + product_series_rec(n - 1)

# Iterative 
# Loops from k=1 up to n accumulating (k-1)*k
def product_sereis_iter(n: int) -> int:
    total = 0
    for k in range(1, n + 1):
        total += (k - 1) * k
    return total

####################################
# - Tests ....
#####################################

# Test Data Setup
n_val = 500
sample_str = "this is a comp sci alsogithms test string"
sample_floats = [-1.5, 2.3, -4.2, 5.0, -9.8, 12.1, -15.4, 20.0] * 10
sample_ints = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] * 10
div_val = 2**20

#.. continue
print("Sample Executions & function ouputs...")
print("=" * 50)

#1. Series Sum
print("1. Series Sum (N=6):", series_sum_rec(6))
