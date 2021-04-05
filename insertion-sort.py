"""
    Write a function that takes in an array of integers and returns a sorted version of that array. Use
    the Insertion Sort algorithm to sort the array.

    Example:
        array = [8, 5, 2, 9, 5, 6, 3]

        Output:
            [2, 3, 5, 5, 6, 8, 9]
"""
# O(n^2) time in the average/worst cases (O(n) time in the best case (sorted array)); O(1) space
def insertionSort(array):
    for i in range(1, len(array)):
        while array[i] < array[i-1] and i > 0:
            array[i], array[i-1] = array[i-1], array[i]
            i -= 1
    return array