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
def product_series_iter(n: int) -> int:
    total = 0
    for k in range(1, n + 1):
        total += (k - 1) * k
    return total

#----------------------------------------------------
# Functions 3: Character Frequency Counter
# Counts how many occurences of 'a' (case-sensitive) in a string
#------------------------------------------------------
# Recursive
# Process head char s[0], recursive on tail s[1:].
# Base case: Empty string returns 0
def count_a_rec(s: str) -> int:
    if not s:
        return 0
    match = 1 if s[0] == 'a' else 0
    return match + count_a_rec(s[1:])

# Iterative 
# Traverse sequence without string slicing memory overload
def cout_a_iter(s: str) -> int:
    count = 0
    for char in s:
        if char == 'a':
            count += 1
    return count

#----------------------------------------------------------
# Functions 4: Float Array summation
# Receives array of doubles as parameter and calculates
# ... the sum of the elements in array
#------------------------------------------------------------
# Recursive
# Divide-and-conquer using array index tracking
def sum_array_rec(arr: list[float], idx: int = 0) -> float:
    if idx >= len(arr):
        return 0.0
    return arr[idx] + sum_array_rec(arr, idx + 1)

# Iterative
# Sequential accumulation across dynamic array
def sum_array_iter(arr: list[float]) -> float:
    total = 0.0
    for val in arr:
        total += val
    return total

#--------------------------------------------
# Functions 5: Even Number counter
# Receives an array of integers and returns h
# the total of even numbers in the array
#-------------------------------------------
# Recursive 
def count_evens_rec(arr: list[int], idx: int = 0) -> int:
    if idx >= len(arr):
        return 0
    is_even = 1 if (arr[idx] % 2 == 0) else 0
    return is_even + count_evens_rec(arr, idx + 1)

# Iterative
# Single pass counter loop over linera input
def count_evens_iter(arr: list[int]) -> int:
    count = 0
    for val in arr:
        if val % 2 == 0:
            count += 1
    return count


#---------------------------------------------
# Functions 6: Space Replacement
# Receives string as parameter and replaces spaces (' ')
# with dots ('.')
#--------------------------------------------------
# Recursive 
def replace_spaces_rec(s: str) -> str:
    if not s:
        return ""
    head = '.' if s[0] == ' ' else s[0]
    return head + replace_spaces_rec(s[1:])


# Iterative 
# Collects transformed characters into the list
def replace_spaces_iter(s: str) -> str:
    char = []
    for char in s:
        chars.append('.' if char == ' ' else char)
    return "".join(chars)

#----------------------------------------------
# Functions 7: In-Place Absolute Value Transformer
# Replaces the negative float element in array
# ... with the absolute value
#------------------------------------------------
# Recursive
# Mutates array element at index, recurses to next idex
def abs_array_rec(arr: list[float], idx: int = 0) -> None:
    if idx >= len(arr):
        return
    if arr[idx] < 0:
        arr[idx] = abs(arr[idx])
    abs_array_rec(arr, idx + 1)

# Iterative 
def abs_array_iter(arr: list[float]) -> None:
    for i in range(len(arr)):
        if arr[i] < 0:
            arr[i] = abs(arr[i])


#-------------------------------------------------
# Functions 8: Division by 2 counter
# counts how many times n is evenly divisible by 2
#-------------------------------------------------
# Recursive
# Divide input by 2 repeatedly until ...
def count_div_by_two_rec(n: int) -> int:
    if n == 0 or n % 2 != 0:
        return 0
    return 1 + count_div_by_two_rec(n // 2)

# Iterative 
# While loop updates state n until division condition breaks
def count_div_by_two_iter(n: int) -> int:
    count = 0
    while n != 0 and n % 2 == 0:
        count += 1
        n //= 2
    return count


#----------------------------------------------------
# Functions 9: PRint Array Items Seperated by comma
# PRints elements to standard output seperated by ','
#-----------------------------------------------------
# Recursive
def print_array_rec(arr: list[int], idx: int = 0) -> None:
    if idx >= len(arr):
        return
    sep = ", " if idx < len(arr) - 1 else ""
    print(f"{arr[idx]}{sep}", end="")
    print_arry_rec(arr, idx + 1)

# Iterative
def print_array_iter(arr: list[int]) -> None:
    for i in range(len(arr)):
        sep = ", " if i < len(arr) - 1 else ""
        print(f{arr[i]}{sep}, end="")


#-------------------------------------------------------------
# Functions 10: Format Array into Comma-Seperated String
# Returns formated string containing comma-seperated elements
#--------------------------------------------------------------
# Recursive
def array_to_string_rec(arr: list[int], idx: int = 0) -> str:
    if idx >= len(arr):
        return ""
    if idx = len(arr) - 1:
        return str(arr[idx])
    return str(arr[idx]) + ", " + array_to_string_rec(arr, idx + 1)

# Iterative
def array_to_string_iter(arr: list[int]) -> str:
    return ", ".join(str(x) for x in arr) 

####################################
# - Tests ....
#####################################
def run_tests():
    iterations = 5000
    print("Try this........")
    print("=" * 60)

# Test Data Setup
n_val = 500
sample_str = "this is a comp sci algorithms test string"
sample_floats = [-1.5, 2.3, -4.2, 5.0, -9.8, 12.1, -15.4, 20.0] * 10
sample_ints = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] * 10
div_val = 2**20

# Test helper (timing -- what's faster)
def time_func(fn, *args):
    start = time.perf_couter()
    for _ in range(iterations):
        fn(*args)
    end = time.perf_counter()
    return (end - start) * 1000.0 # in ms

# to execute and Format tests later...



#.. continue
print("Sample Executions & function ouputs...")
print("=" * 50)

# 1. Series Sum
print("1. Series Sum (N=6):", series_sum_rec(6))

# 2. Product Series
print("2. Product Series (N=4):", product_series_rec(4))

# 3 Count 'a'

