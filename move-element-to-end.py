"""
    You're given an array of integers and an integer. Write a function that moves
    all instances of that integer in the array to the end of the array and returns
    the array.

    The function should perform this in place (i.e., it should mutate the input
    array) and doesn't need to maintain the order of the other integers.

    Example:
        array = [2, 1, 2, 2, 2, 3, 4, 2]
        toMove = 2

        Output:
            [1, 3, 4, 2, 2, 2, 2, 2]
            # Note that the numbers 1, 3, 4 can be ordered differently
"""
def moveElementToEnd(array, toMove):
	for i in reversed(range(len(array))):
		if array[i] == toMove:
			del array[i]
			array.append(toMove)		
	return array