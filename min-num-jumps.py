"""
    You're given a non-empty array of positive integers where each integer represents the
    maximum number of steps you can take forward in the array. For example, if the
    element at index 1 is 3, you can go from index 1 to index 2, 3, or 4.

    Write a function that returns the minimum number of jumps needed to reach the final index.

    Note that jumping from index i to index i + x always constitutes one jump, no matter how large x is.

    Example:
        array = [3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]

        Output:
            4 
"""
def minNumberOfJumps(array):
    final_idx = len(array) - 1
    jumps_from_idx = [0 for _ in range(len(array))]
    
    for i in range(len(array)-2, -1, -1):
        item = array[i]
        options = []

        for x in range(1, item+1):
            if i + x >= final_idx:
                options.append(1)
            else:
                options.append(1 + jumps_from_idx[i + x])

        # jumps_from_idx[i] = min([x for x in range(1, item+1) if x + i >= final_idx])
        jumps_from_idx[i] = min(options)
        print(jumps_from_idx[i])

    return jumps_from_idx[0]


# def jump_helper(array, idx, jump_count=0):
    
#     for 



# def minNumberOfJumps(array):
#     return jump_helper(array, 0, 0)

# def jump_helper(array, idx, jump_count=0):
    
#     if idx >= len(array) - 1:
#         print(idx)
#         return jump_count

#     for i in range(idx, len(array)):
#         jump_helper(array, idx + array[i], jump_count + 1)        

# assert minNumberOfJumps([3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]) == 4
print(minNumberOfJumps([3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]))