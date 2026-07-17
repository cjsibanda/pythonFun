"""
--------------------------------------------------------
Author: CJ

Testing concepts:
--> Recursion
--> Binary Search
--> Selection Sort
--> Merge (used in Merge Sort)

understand HOW each algorithm works
--------------------------------------------------------
"""


# ======================================================
# RECURSION
# ======================================================

def factorial(n):
    """
    Calculates n! using recursion.

    Every recursive function has TWO important parts:

    1. Base Case
       The stopping condition.
       Without it, the function would call itself forever.

    2. Recursive Case
       Solve a smaller version of the same problem.

    Example:
        factorial(4)

        = 4 * factorial(3)
        = 4 * 3 * factorial(2)
        = 4 * 3 * 2 * factorial(1)
        = 4 * 3 * 2 * 1
        = 24
    """

    # -------------------------
    # Base Case
    # -------------------------
    if n <= 1:
        return 1

    # -------------------------
    # Recursive Case
    # -------------------------
    return n * factorial(n - 1)


print("========== RECURSION ==========")
print("Factorial of 5 =", factorial(5))
print()


# ======================================================
# BINARY SEARCH
# ======================================================

def binary_search(numbers, target):
    """
    Binary Search ONLY works on a sorted list.

    Instead of checking every element,
    it repeatedly cuts the search space in half.

    Time Complexity:
        O(log n)

    faster than checking every element.
    """

    low = 0
    high = len(numbers) - 1

    while low <= high:

        # Find the middle index
        middle = (low + high) // 2

        print(f"Checking index {middle} (value = {numbers[middle]})")

        if numbers[middle] == target:
            return middle

        elif target < numbers[middle]:
            # Target must be in the LEFT half
            high = middle - 1

        else:
            # Target must be in the RIGHT half
            low = middle + 1

    return -1


print("========== BINARY SEARCH ==========")

sorted_numbers = [2, 5, 7, 9, 13, 18, 21, 27]

index = binary_search(sorted_numbers, 18)

print("18 found at index:", index)
print()


# ======================================================
# SELECTION SORT
# ======================================================

def selection_sort(numbers):
    """
    Selection Sort repeatedly finds the smallest
    remaining value and places it into its correct
    position.

    NOTE:

    While searching,
    NOTHING moves.

    We simply remember the location of the
    smallest value.

    Only ONE swap happens after each pass.

    Time Complexity:
        O(n²)
    """

    n = len(numbers)

    for i in range(n - 1):

        # Assume the current position
        # contains the smallest value.
        smallest = i

        # Search the remaining list
        for j in range(i + 1, n):

            if numbers[j] < numbers[smallest]:
                smallest = j

        # Swap only if needed
        if smallest != i:
            numbers[i], numbers[smallest] = numbers[smallest], numbers[i]

        print(f"After pass {i + 1}: {numbers}")


print("========== SELECTION SORT ==========")

values = [8, 3, 6, 1, 9]

print("Original List:", values)

selection_sort(values)

print("Sorted List:", values)
print()


# ======================================================
# MERGE
# ======================================================

def merge(left, right):
    """
    Merge combines TWO already sorted lists
    into ONE sorted list.

    Example:

    Left:
        [2, 5, 8]

    Right:
        [1, 4, 9]

    Result:
        [1, 2, 4, 5, 8, 9]

    Merge is the most important step
    inside Merge Sort.
    """

    merged = []

    left_index = 0
    right_index = 0

    # Compare the first unused value
    # from each list.
    while left_index < len(left) and right_index < len(right):

        if left[left_index] <= right[right_index]:

            merged.append(left[left_index])
            left_index += 1

        else:

            merged.append(right[right_index])
            right_index += 1

    # Copy any remaining values
    # from the left list.
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    # Copy any remaining values
    # from the right list.
    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


print("========== MERGE ==========")

left = [2, 5, 8]
right = [1, 4, 9]

print("Left List :", left)
print("Right List:", right)

merged = merge(left, right)

print("Merged List:", merged)

print()

print("========== THE END ==========")