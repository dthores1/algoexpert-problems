"""
	You're given two positive integers representing the height of a staircase and
	the maximum number of steps that you can advance up the staircase at a time.
	Write a function that returns the number of ways in which you can climb the
	staircase.

	For example, if you were given a staircase of height = 3 and
	maxSteps = 2 you could climb the staircase in 3 ways. You could
	take 1 step, 1 step, then 1 step, you could also take
	1 step, then 2 steps, and you could take 2 steps, then 1 step.

	Note that maxSteps <= height will always be true.
	
	Example:
		height = 4
		maxSteps = 2

	Output: 5
		// You can climb the staircase in the following ways: 
		// 1, 1, 1, 1
		// 1, 1, 2
		// 1, 2, 1
		// 2, 1, 1
		// 2, 2
"""
def staircaseTraversal(height, maxSteps):
	cache = [0 for _ in range(height + 1)]
	cache[0] = 1 # Only one way to make zero steps!

	for i in range(height + 1):
		cache[i] += sum(cache[i - x] for x in range(1, maxSteps+1) if i - x >= 0)
	
	return cache[height]

assert staircaseTraversal(7,2) == 21
assert staircaseTraversal(6,2) == 13
assert staircaseTraversal(5,2) == 8
assert staircaseTraversal(4,2) == 5