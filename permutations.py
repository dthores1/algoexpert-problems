"""
    Write a function that takes in an array of unique integers and returns an
    array of all permutations of those integers in no particular order.

    If the input array is empty, the function should return an empty array.

    Example:
        array = [1, 2, 3]
    Output:
        [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

"""

def getPermutations(array):
	results = []
	make_permutations(0, array, results)
	return results

def make_permutations(idx, array, results):
	if idx == (len(array) - 1):
		results.append(array[:])
		
	for j in range(idx, len(array)):
		array[j], array[idx] = array[idx], array[j]
		make_permutations(idx + 1, array, results)
		array[j], array[idx] = array[idx], array[j]


print(permutations([1, 2, 3]))