"""
    Write a function that takes in a sorted array of integers as well as a target
    integer. The function should use a variation of the Binary Search algorithm to
    find a range of indices in between which the target number is contained in the
    array and should return this range in the form of an array.

    The first number in the output array should represent the first index at which
    the target number is located, while the second number should represent the
    last index at which the target number is located. The function should return
    [-1, -1] if the integer isn't contained in the array.

    If you're unfamiliar with Binary Search, we recommend watching the Conceptual
    Overview section of the Binary Search question's video explanation before
    starting to code.

    Example:
        array = [0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73]
        target = 45

        Output:
            [4, 9]

"""
def searchForRange(array, target):
    final_range = [-1, -1]
    binary_search(array, target, "LEFT", final_range)
    binary_search(array, target, "RIGHT", final_range)
    return final_range

# Return a tuple of the idx in question, and the best we know from the other direction
def binary_search(array, target, direction, final_range):
    left, right = 0, len(array) - 1

    while left <= right:
        pivot = (left + right) // 2

        if array[pivot] == target:
            if direction == "LEFT":
                if pivot == 0 or array[pivot - 1] != target:
                    final_range[0] = pivot
                    return
                else:
                    right = pivot - 1
            else:
                if pivot == len(array) - 1 or array[pivot + 1] != target:
                    final_range[1] = pivot
                    return
                else:
                    left = pivot + 1
                
        elif array[pivot] < target:
            left = pivot + 1
        elif array[pivot] > target:+
            right = pivot - 1

assert searchForRange([0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73], 45) == [4, 9]
assert searchForRange([5, 7, 7, 8, 8, 10], 7) == [1, 2]