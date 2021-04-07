"""
    Write a function that takes in a non-empty array of arbitrary intervals,
    merges any overlapping intervals, and returns the new intervals in no
    particular order.

    Each interval is an array of two integers, with interval[0] as the start of the
    interval and interval[1] as the end of the interval.

    Note that back-to-back intervals aren't considered to be overlapping. For example 
    [1, 5] and [6, 7] aren't overlapping; however, [1, 6] and [6, 7] are indeed 
    overlapping.

    Also note that the start of any particular interval will always be less than or equal
    to the end of that interval.

    Example:
        intervals = [[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]

        Output:
            [[1, 2], [3, 8], [9, 10]]
"""
# O(n log(n)) due to the sorting 
def mergeOverlappingIntervals(intervals):
    intervals = sorted(intervals, key=lambda x: x[0])
    results = [intervals[0]]

    for index in range(1, len(intervals)):
        this_interval = intervals[index]     

        if this_interval[0] <= results[-1][1]:
            results[-1] = [min(results[-1][0], this_interval[0]), max(this_interval[1], results[-1][1])]
        else:
            results.append(this_interval)

    return results