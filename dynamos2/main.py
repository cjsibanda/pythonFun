"""
------------------------------------------------------------
Sorting Algorithms
Author: CJ

--> demonstrating four important algorithms:

1. Merge Sort
2. Merge Function
3. Quick Sort (Partition)
4. Insertion Sort

understand HOW each algorithm works.
------------------------------------------------------------
"""

import random


# ==========================================================
# MERGE SORT
# ==========================================================

def merge_sort(numbers):
    """
    -Merge Sort uses the Divide and Conquer strategy.
    -Instead of sorting the entire list at once,
    it repeatedly splits the list into smaller pieces.
    -Once every piece contains only one element,
    those pieces are merged back together in sorted order.

    Time Complexity:
        O(n log n)

    -This is faster than Selection Sort (O(n²))
    for large lists.
    """

    # Create one temporary list.
    # Reusing it is more efficient than creating
    # a new list every time we merge.
    temp = [0] * len(numbers)

    recursive_merge_sort(numbers, 0, len(numbers) - 1, temp)


def recursive_merge_sort(numbers, left, right, temp):
    """
    -Recursive Merge Sort

    -Base Case:
        A list with one element is already sorted.

    -Recursive Case:
        Split the list into two halves,
        sort each half,
        then merge them together.
    """

    # Base Case
    if left >= right:
        return

    # Find the middle index
    middle = (left + right) // 2

    # Recursively sort left half
    recursive_merge_sort(numbers, left, middle, temp)

    # Recursively sort right half
    recursive_merge_sort(numbers, middle + 1, right, temp)

    # Merge the two sorted halves
    merge(numbers, left, middle + 1, right, temp)


# ==========================================================
# MERGE FUNCTION
# ==========================================================

def merge(numbers, left_start, right_start, right_end, temp):
    """
    -Merge combines TWO sorted sections into ONE larger
    sorted section.

    Example

    Left:
        2 5 8

    Right:
        1 4 9

    Result:
        1 2 4 5 8 9

    This function does NOT sort.

    It assumes BOTH halves are already sorted.
    """

    left = left_start
    right = right_start
    index = left_start

    # Compare the front element of each half
    while left < right_start and right <= right_end:

        if numbers[left] <= numbers[right]:
            temp[index] = numbers[left]
            left += 1
        else:
            temp[index] = numbers[right]
            right += 1

        index += 1

    # Copy remaining values
    while left < right_start:
        temp[index] = numbers[left]
        left += 1
        index += 1

    while right <= right_end:
        temp[index] = numbers[right]
        right += 1
        index += 1

    # Copy sorted values back
    for i in range(left_start, right_end + 1):
        numbers[i] = temp[i]


# ==========================================================
# INSERTION SORT
# ==========================================================

def insertion_sort(numbers):
    """
    -Insertion Sort works like sorting playing cards.
    -Imagine your left hand is already sorted.
    -Pick up one new card.
    -Shift larger cards to the right until
    -the correct position is found.

    -Insert the new card.

    Time Complexity:
        O(n²)

    However...

    It performs very well when the list
    is already mostly sorted.
    """

    for i in range(1, len(numbers)):

        current = numbers[i]

        j = i

        # Shift larger values right
        while j > 0 and numbers[j - 1] > current:
            numbers[j] = numbers[j - 1]
            j -= 1

        numbers[j] = current


# ==========================================================
# PARTITION (Quick Sort)
# ==========================================================

def partition(numbers, left, right):
    """
    -Partition is the IMPORTANT part
    of Quick Sort.
    -It chooses one value called the Pivot.
    -Every value smaller than the pivot
    moves to the left.
    -Every value larger than the pivot
    moves to the right.
    -Finally the pivot is placed between them.
    -The function returns the pivot's
    final position.
    """

    # Pick a random pivot
    pivot_index = random.randint(left, right)

    pivot = numbers[pivot_index]

    # Move pivot to the end
    numbers[pivot_index], numbers[right] = numbers[right], numbers[pivot_index]

    end_of_small = left - 1

    for i in range(left, right):

        if numbers[i] <= pivot:
            end_of_small += 1

            numbers[end_of_small], numbers[i] = numbers[i], numbers[end_of_small]

    # Put pivot in its final location
    numbers[end_of_small + 1], numbers[right] = (
        numbers[right],
        numbers[end_of_small + 1]
    )

    return end_of_small + 1


# ==========================================================
# RECURSIVE QUICK SORT
# ==========================================================

def quick_sort(numbers, left, right):
    """
    -Recursive Quick Sort
    -Base Case:
        Zero or one element.
    -Recursive Case:
        -Partition the list.
        -Everything left of the pivot
        is sorted recursively.
        -Everything right of the pivot
        is sorted recursively.
    """

    if left >= right:
        return

    pivot = partition(numbers, left, right)

    quick_sort(numbers, left, pivot - 1)
    quick_sort(numbers, pivot + 1, right)


# ==========================================================
# MAIN PROGRAM
# ==========================================================

def main():

    print("========== MERGE SORT ==========")

    values = [9, 4, 7, 2, 8, 1, 5]

    print("Original:", values)

    merge_sort(values)

    print("Sorted  :", values)

    print()

    print("========== INSERTION SORT ==========")

    values = [6, 2, 8, 3, 9, 1]

    print("Original:", values)

    insertion_sort(values)

    print("Sorted  :", values)

    print()

    print("========== QUICK SORT ==========")

    values = [10, 4, 8, 1, 6, 3, 9]

    print("Original:", values)

    quick_sort(values, 0, len(values) - 1)

    print("Sorted  :", values)


if __name__ == "__main__":
    main()