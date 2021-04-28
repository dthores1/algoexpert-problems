"""
    You're given an array of integers where each integer represents a jump of its
    value in the array. For instance, the integer <span>2</span> represents a jump
    of two indices forward in the array; the integer <span>-3</span> represents a
    jump of three indices backward in the array.


    If a jump spills past the array's bounds, it wraps over to the other side. For
    instance, a jump of <span>-1</span> at index <span>0</span> brings us to the last index in
    the array. Similarly, a jump of <span>1</span> at the last index in the array brings us to
    index <span>0</span>.


    Write a function that returns a boolean representing whether the jumps in the
    array form a single cycle. A single cycle occurs if, starting at any index in
    the array and following the jumps, every element in the array is visited
    exactly once before landing back on the starting index.

    Example:
        array = [2, 3, 1, -4, -4, 2]

        Output: true
"""
def hasSingleCycle(array):
	visited = [False]*len(array)
	num_visited = 0
	idx = get_index(array[0], array)
	
	while num_visited < len(array):
		if visited[idx]:
			return False
		
		num_visited += 1		
		visited[idx] = True
		
		idx += array[idx]
		idx = get_index(idx, array)
		
	return True

def get_index(idx, array):
	if idx == len(array):
		return 0
	elif abs(idx) > len(array):
		while abs(idx) > len(array):
			if idx > 0:
				idx -= len(array)
			else:
				idx += len(array)
	
	return idx