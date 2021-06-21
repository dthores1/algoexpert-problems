"""
    Given a non-empty array of integers, write a function that returns the longest 
    strictly-increasing subsequence in the array.

    A subsequence of an array is a set of numbers that aren't necessarily adjacent
    in the array but that are in the same order as they appear in the array. For
    instance, the numbers [1, 3, 4] form a subsequence of the array
    [1, 2, 3, 4], and so do the numbers [2, 4]. Note
    that a single number in an array and the array itself are both valid
    subsequences of the array.

    You can assume that there will only be one longest increasing subsequence.

    Example:
        array = [5, 7, -24, 12, 10, 2, 3, 12, 5, 6, 35]

        Output:
            [-24, 2, 3, 5, 6, 35]
"""
def longestIncreasingSubsequence(array):
    if array == []:
        return []

    results = {
        0: [array[0]]
    }

    overall_best = results[0]

    for idx in range(1, len(array)):
        best_so_far = [array[idx]]

        for idx2 in range(idx):
            comparison = array[idx2]

            if array[idx] > comparison and (len(results[idx2]) + 1) > len(best_so_far):
                best_so_far = results[idx2] + [array[idx]]

        results[idx] = best_so_far
        if len(best_so_far) > len(overall_best):
            overall_best = best_so_far

    return overall_best

print(longestIncreasingSubsequence([5, 7, -24, 12, 10, 2, 3, 12, 5, 6, 35])) # [-24, 2, 3, 5, 6, 35]