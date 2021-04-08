"""
    Write a function that takes in two non-empty arrays of integers, finds the
    pair of numbers (one from each array) whose absolute difference is closest to
    zero, and returns an array containing these two numbers, with the number from
    the first array in the first position.

    Note that the absolute difference of two integers is the distance between
    them on the real number line. For example, the absolute difference of -5 and 5
    is 10, and the absolute difference of -5 and -4 is 1.

    You can assume that there will only be one pair of numbers with the smallest
    difference.

    Example:
        arrayOne = [-1, 5, 10, 20, 28, 3]
        arrayTwo = [26, 134, 135, 15, 17]

        Output:
            [28, 26]
"""
def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()

    results = []
    smallest_diff_so_far = None

    i, j = 0, 0

    while i < len(arrayOne) and j < len(arrayTwo):
        if arrayOne[i] == arrayTwo[j]:
            return [arrayOne[i], arrayTwo[j]]

        if smallest_diff_so_far is None or smallest_diff_so_far > abs(arrayOne[i] - arrayTwo[j]):
            smallest_diff_so_far = abs(arrayOne[i] - arrayTwo[j])
            results = [arrayOne[i], arrayTwo[j]]

        if arrayOne[i] < arrayTwo[j]:
            i += 1
        else: 
            j += 1


    return results