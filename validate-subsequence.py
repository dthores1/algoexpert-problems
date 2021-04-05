"""
    Given two non-empty arrays of integers, write a function that determines whether the second array is a 
    subsequence of the first one. 

    A subsequence of an array is a set of numbers that aren't necessarily adjacent in the array but that are
    in the same order as they appear in the array. For instance, the numbers [1, 3, 4] form a subsequence of
    the array [1, 2, 3, 4] and so do the numbers [2, 4]. Not that a single number in an array and the array 
    itself are both valid subsequences of the array.

    Example:

        array = [5, 1, 22, 25, 6, -1, 8, 10]
        sequence = [1, 6, -1, 10]

        Output:
            True
"""

# Complexity - O(n) time / O(1) space
def isValidSubsequence(array, sequence):
	# Start with the first index of the subsequence array; every time we 
    # find a number in the actual array, we'll increment this number
    index_to_check = 0
	
	for i in array:
		if i == sequence[index_to_check]:
			index_to_check += 1
		
        # If we found the whole sequence, return True
		if index_to_check > len(sequence) - 1:
			return True
	
    # If we haven't returned True by this point, the subsequence is not in the array
	return False