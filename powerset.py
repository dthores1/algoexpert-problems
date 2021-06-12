"""
    Write a function that takes in an array of unique integers and returns its
    powerset.

    The powerset P(X) of a set X is the set of all
    subsets of X. For example, the powerset of [1,2] is
    [[], [1], [2], [1,2]].

    Note that the sets in the powerset do not need to be in any particular order.

    Example:
        array = [1, 2, 3]

        Output:
            [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
"""
def powerset(array):
    subsets = [[]]

    for element in array:
        for n in range(len(subsets)):
            current = subsets[n]
            subsets.append(current + [element])

    return subsets

print(powerset([1, 2, 3]))