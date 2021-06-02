"""
    Write a function that takes in a non-empty array of integers and returns the
    greatest sum that can be generated from a strictly-increasing subsequence in
    the array as well as an array of the numbers in that subsequence.

    A subsequence of an array is a set of numbers that aren't necessarily adjacent
    in the array but that are in the same order as they appear in the array. For
    instance, the numbers [1, 3, 4] form a subsequence of the array
    [1, 2, 3, 4], and so do the numbers [2, 4]. Note
    that a single number in an array and the array itself are both valid
    subsequences of the array.

    You can assume that there will only be one increasing subsequence with the greatest sum.

    Example:
        array = [10, 70, 20, 30, 50, 11, 30]


        Output:[110, [10, 20, 30, 50]] # The subsequence [10, 20, 30, 50] is strictly increasing and yields the greatest sum: 110.
"""
def maxSumIncreasingSubsequence(array):
    results = [ [array[0], [array[0]]] ]
    overall_best = results[0]

    for i in range(1, len(array)):
        best_so_far = [-float("inf"), []]

        for j in range(i-1, -1, -1):
            if array[j] < array[i] and results[j][0] > best_so_far[0]:
                best_so_far = results[j]

        if best_so_far[0] != -float("inf"):
            res_array = [x for x in best_so_far[1]]
            res_array.append( array[i] )
            results.append([best_so_far[0] + array[i], res_array])
        else:
            best_so_far = [array[i], [array[i]]]
            results.append(best_so_far)

        if results[-1][0] > overall_best[0]:
            overall_best = results[-1]

    # Try the last element as a standalone since we didn't consider it yet
    return overall_best if overall_best[0] > array[-1] else [array[-1], [array[-1]]]