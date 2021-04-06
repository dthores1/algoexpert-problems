"""
    Write a function that takes in a sorted array of integers as well as a target
    integer. The function should use the Binary Search algorithm to determine if
    the target integer is contained in the array and should return its index if it
    is, otherwise -1.

    Example:
        array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
        target = 33

        Result: 3
"""

def binarySearch(array, target):
    min, max = 0, len(array)
    finished = False
    while not finished:
        mid = (max + min) // 2

        # If we hit the target or the indices are adjacent, we're done
        if array[mid] == target:
            return mid
        elif max - min == 1:
            if array[max] == target:
                return max
            elif array[min] == target:
                return min
            
            finished = True

        # Keep shifting the search indices depending on the middle element's value relative to the target
        if target < array[mid]:
            max = mid
        else:
            min = mid

    return -1