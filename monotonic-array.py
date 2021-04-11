"""
    Write a function that takes in an array of integers and returns a boolean
    representing whether the array is monotonic.

    An array is said to be monotonic if its elements, from left to right, are
    entirely non-increasing or entirely non-decreasing.

    Non-increasing elements aren't necessarily exclusively decreasing; they simply
    don't increase. Similarly, non-decreasing elements aren't necessarily
    exclusively increasing; they simply don't decrease.

    Note that empty arrays and arrays of one element are monotonic.
    
    Example:
        array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
    Output:
        True
"""

def isMonotonic(array):
	status_not_determined = True
	increases = False
	decreases = False
	
	for i in range(1, len(array)):
		if array[i] != array[i-1]:
			if (increases and array[i] < array[i-1]) or (decreases and array[i] > array[i-1]):
				return False
			elif status_not_determined:
				status_not_determined = False
				decreases = array[i] < array[i-1]
				increases = not decreases
		
	return True