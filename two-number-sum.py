"""
Write a function that takes a non-empty array of distinct integers and an integer representing a target sum.
If any two numbers in the input array sum up to the target sum, the function should return them in an array, 
in any order. If no two numbers sum up to the target sum, the function should return an empty array. 

Note that the target sum has to be obtained by summing two different integers in the array; you can't add a 
single integer to itself in order to obtain the target sum.

You can assume there will be at most one pair of numbers summing up to the target sum. 

Example:
    array = [3, 5, -4, 8, 11, 1, -1, 6]
    targetSum = 10

    Output: [1, 11]
"""

# This uses O(n) time, traversing the array once
def twoNumberSum(array, targetSum):

	numbers_tried = set()
	result = []
	
	for i in array:
		
		needed_number = targetSum - i
		
		if needed_number in numbers_tried:
			result = [needed_number, i]
			return result
		
		numbers_tried.add(i)
		
	return result